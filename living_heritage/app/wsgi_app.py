"""
WSGI adapter — lets this stdlib HTTP app run under WSGI hosting
(e.g. PythonAnywhere), which cannot run raw socket servers.

Exposes a standard `application(environ, start_response)` that reuses the
router's route table, not-found handler, and static-file logic.
"""
import os
import mimetypes
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs

from app.router import (
    routes,
    _parse_pattern,
    _not_found_handler,
    Request,
    Response,
    STATIC_DIR,
)

# Registers the app's routes (decorators run at app.main import time); the
# classic `python -m app.main` path imports it directly, whereas WSGI hosts
# only import this module, so we must ensure the route table is populated.
import app.main  # noqa: F401


def _application(environ, start_response):
    method = environ.get("REQUEST_METHOD", "GET")
    path = environ.get("PATH_INFO", "/") or "/"
    query = parse_qs(environ.get("QUERY_STRING", ""))

    content_length = int(environ.get("CONTENT_LENGTH", "0") or "0")
    body = environ["wsgi.input"].read(content_length) if content_length > 0 else b""

    # Cookie header: WSGI names it HTTP_COOKIE
    cookie_header = environ.get("HTTP_COOKIE", "")
    cookies = {}
    for pair in cookie_header.split(";"):
        pair = pair.strip()
        if "=" in pair:
            k, v = pair.split("=", 1)
            cookies[k.strip()] = v.strip()

    # Merge form body into query for POST (same behavior as router.Handler)
    if method == "POST" and body:
        ct = environ.get("CONTENT_TYPE", "")
        if "application/x-www-form-urlencoded" in ct:
            query.update(parse_qs(body.decode("utf-8")))

    try:
        handler, req = _match_wsgi(method, path, query, cookies, body, environ)
        if handler and req:
            result = handler(req)
            if isinstance(result, str):
                result = Response.html(result)
        else:
            result = _serve_static_wsgi(path, cookies)
    except Exception:  # noqa: BLE001 — never leak a traceback to the client
        if os.environ.get("LH_WSGI_DEBUG"):
            import traceback
            result = Response.html(
                "Internal Server Error\n\n" + traceback.format_exc(), 500
            )
        else:
            result = Response.html("Internal Server Error", 500)

    status = f"{result.status} {HTTPStatus(result.status).phrase}"
    headers = [
        ("Content-Type", result.content_type),
        ("Content-Length", str(len(result.body))),
    ]
    for k, v in result.headers.items():
        headers.append((k, v))
    for name, value in result.cookies.items():
        headers.append(("Set-Cookie", f"{name}={value}; Path=/; Max-Age=31536000"))
    start_response(status, headers)
    return [result.body]


def _wsgi_headers(environ):
    """Reconstruct HTTP header names from WSGI environ (HTTP_* / CONTENT_*)."""
    req_headers = {}
    for key, value in environ.items():
        if key.startswith("HTTP_"):
            name = key[5:].replace("_", "-").title()
            req_headers[name] = value
        elif key in ("CONTENT_TYPE", "CONTENT_LENGTH"):
            req_headers[key.replace("_", "-").title()] = value
    return req_headers


def _match_wsgi(method, path, query, cookies, body, environ):
    method_routes = routes.get(method, {})
    for route_path, route_info in method_routes.items():
        m = route_info["regex"].match(path)
        if m:
            params = dict(zip(route_info["params"], m.groups()))
            req = Request(
                method=method, path=path, query=query,
                headers=_wsgi_headers(environ), body=body,
                cookies=cookies, params=params,
            )
            return route_info["handler"], req
    return None, None


def _serve_static_wsgi(path, cookies):
    file_path = (STATIC_DIR / path.lstrip("/")).resolve()
    # Security: ensure within static dir
    if str(file_path).startswith(str(STATIC_DIR.resolve())):
        if file_path.is_file():
            ct, _ = mimetypes.guess_type(str(file_path))
            ct = ct or "application/octet-stream"
            return Response(file_path.read_bytes(), content_type=ct)
    if _not_found_handler:
        try:
            return _not_found_handler(path, cookies)
        except Exception:  # noqa: BLE001
            pass
    return Response.html("Not Found", 404)


application = _application

# Convenience alias often expected by WSGI hosts
app = application