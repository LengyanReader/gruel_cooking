"""
Minimal HTTP router — no framework dependency.
Handles routing, static files, cookies, and template responses.
"""
import os
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from functools import wraps
from pathlib import Path
from typing import Callable
from app.config import STATIC_DIR as _STATIC, AVAILABLE_LOCALES, DEFAULT_LOCALE

STATIC_DIR = _STATIC
routes: dict[str, dict[str, Callable]] = {}  # method -> {path_pattern: handler}


def _parse_pattern(pattern: str):
    """Convert '/corridors/<slug>' to regex and param names."""
    import re
    param_names = []
    regex_parts = []
    for part in pattern.strip("/").split("/"):
        if part.startswith("<") and part.endswith(">"):
            param_names.append(part[1:-1])
            regex_parts.append(r"([^/]+)")
        else:
            regex_parts.append(re.escape(part))
    regex = r"^/" + r"/".join(regex_parts) + r"/?$"
    return re.compile(regex), param_names


def route(path: str, methods: list[str] | None = None):
    """Decorator to register a route handler."""
    def decorator(func: Callable):
        m = methods if methods is not None else ["GET"]
        pattern_re, param_names = _parse_pattern(path)
        for method in m:
            routes.setdefault(method.upper(), {})[path] = {
                "regex": pattern_re,
                "params": param_names,
                "handler": func,
            }
        return func
    return decorator


def get(path: str):
    return route(path, methods=["GET"])


def post(path: str):
    return route(path, methods=["POST"])


# Optional app-level 404 page: fn(request_path) -> Response. Set via set_not_found_handler.
_not_found_handler = None


def set_not_found_handler(fn):
    global _not_found_handler
    _not_found_handler = fn


class Request:
    """Lightweight request object."""
    def __init__(self, method: str, path: str, query: dict, headers: dict,
                 body: bytes, cookies: dict, params: dict):
        self.method = method
        self.path = path
        self.query = query
        self.headers = headers
        self.body = body
        self.cookies = cookies
        self.params = params

    @property
    def locale(self) -> str:
        return self.cookies.get("locale", DEFAULT_LOCALE)


class Response:
    """Lightweight response object."""
    def __init__(self, content: str | bytes, status: int = 200,
                 content_type: str = "text/html; charset=utf-8",
                 headers: dict | None = None, cookies: dict | None = None):
        if isinstance(content, str):
            self.body = content.encode("utf-8")
        else:
            self.body = content
        self.status = status
        self.content_type = content_type
        self.headers = headers or {}
        self.cookies = cookies or {}

    @classmethod
    def html(cls, content: str, status: int = 200, **kwargs):
        return cls(content, status=status, content_type="text/html; charset=utf-8", **kwargs)

    @classmethod
    def json(cls, data, status: int = 200):
        import json
        body = json.dumps(data, ensure_ascii=False, default=str)
        return cls(body, status=status, content_type="application/json; charset=utf-8")

    @classmethod
    def redirect(cls, url: str, status: int = 303):
        return cls(b"", status=status, headers={"Location": url})


class Handler(BaseHTTPRequestHandler):
    """Single handler for all requests."""

    def log_message(self, format, *args):
        # Quieter logging
        pass

    def _send_response(self, resp: Response):
        self.send_response(resp.status)
        self.send_header("Content-Type", resp.content_type)
        self.send_header("Content-Length", str(len(resp.body)))
        for k, v in resp.headers.items():
            self.send_header(k, v)
        for name, value in resp.cookies.items():
            self.send_header("Set-Cookie", f"{name}={value}; Path=/; Max-Age=31536000")
        self.end_headers()
        self.wfile.write(resp.body)

    def _parse_cookies(self) -> dict:
        cookie_header = self.headers.get("Cookie", "")
        cookies = {}
        for pair in cookie_header.split(";"):
            pair = pair.strip()
            if "=" in pair:
                k, v = pair.split("=", 1)
                cookies[k.strip()] = v.strip()
        return cookies

    def _read_body(self) -> bytes:
        length = int(self.headers.get("Content-Length", 0))
        return self.rfile.read(length) if length > 0 else b""

    def _match_route(self, method: str):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)
        cookies = self._parse_cookies()
        body = self._read_body()

        # Parse form body for POST
        form_data = {}
        if method == "POST" and body:
            ct = self.headers.get("Content-Type", "")
            if "application/x-www-form-urlencoded" in ct:
                form_data = parse_qs(body.decode("utf-8"))

        method_routes = routes.get(method, {})
        for route_path, route_info in method_routes.items():
            m = route_info["regex"].match(path)
            if m:
                params = dict(zip(route_info["params"], m.groups()))
                req = Request(
                    method=method, path=path, query=query,
                    headers=dict(self.headers), body=body,
                    cookies=cookies, params=params,
                )
                # Merge form data into query for POST
                if form_data:
                    req.query.update(form_data)
                return route_info["handler"], req

        return None, None

    def _handle(self, method: str):
        handler, req = self._match_route(method)
        if handler and req:
            result = handler(req)
            if isinstance(result, Response):
                self._send_response(result)
            elif isinstance(result, str):
                self._send_response(Response.html(result))
            else:
                self._send_response(Response.html("Internal Server Error", 500))
        else:
            self._serve_static()

    def _parse_cookies(self) -> dict:
        cookies = {}
        for part in self.headers.get("cookie", "").split(";"):
            if "=" in part:
                k, v = part.strip().split("=", 1)
                cookies[k] = v
        return cookies

    def _not_found_response(self, path: str) -> Response:
        if _not_found_handler:
            try:
                return _not_found_handler(path, self._parse_cookies())
            except Exception:  # noqa: BLE001 — never let the error page break the response
                pass
        return Response.html("Not Found", 404)

    def _serve_static(self):
        parsed = urlparse(self.path)
        file_path = STATIC_DIR / parsed.path.lstrip("/")
        file_path = file_path.resolve()
        # Security: ensure within static dir
        if not str(file_path).startswith(str(STATIC_DIR.resolve())):
            self._send_response(self._not_found_response(self.path))
            return
        if file_path.is_file():
            ct, _ = mimetypes.guess_type(str(file_path))
            ct = ct or "application/octet-stream"
            data = file_path.read_bytes()
            self._send_response(Response(data, content_type=ct))
        else:
            self._send_response(self._not_found_response(self.path))

    def do_GET(self):
        self._handle("GET")

    def do_POST(self):
        self._handle("POST")


def run_server(host: str = "127.0.0.1", port: int = 0):
    if port == 0:
        port = int(os.getenv("LH_PORT", "8000"))
    server = HTTPServer((host, port), Handler)
    print(f"Living Heritage running at http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()
