"""
Boot sequence: init DB → seed if empty → run server.
Kept separate from the route definitions so main.py stays a pure route module.
"""
from app.db.sqlite import init_db
from app.seed import seed_if_empty
from app.router import run_server


def boot(host: str = "127.0.0.1", port: int = 0):
    init_db()
    seed_if_empty()
    run_server(host=host, port=port)