"""
Thin CLI wrapper around app.seed (the canonical seeding implementation).
Run: python scripts/seed_content.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.db.sqlite import init_db  # noqa: E402
from app.seed import seed_all  # noqa: E402


def seed_if_empty():
    from app.seed import seed_if_empty as _f
    _f()


if __name__ == "__main__":
    init_db()
    seed_all()