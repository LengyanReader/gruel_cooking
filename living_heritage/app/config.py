"""
Configuration — all from environment, nothing hardcoded.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# SQLite
SQLITE_PATH = os.getenv("LH_SQLITE_PATH", str(BASE_DIR / "data" / "living_heritage.db"))
SEEDS_DIR = Path(os.getenv("LH_SEEDS_DIR", str(BASE_DIR / "data" / "seeds")))

# Graph engine: "sqlite" (default, zero-dependency) or "neo4j" (optional analysis layer)
GRAPH_ENGINE = os.getenv("LH_GRAPH_ENGINE", "sqlite")

# Neo4j (used only when GRAPH_ENGINE == "neo4j")
NEO4J_URI = os.getenv("LH_NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("LH_NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("LH_NEO4J_PASSWORD", "")

# Locale
DEFAULT_LOCALE = os.getenv("LH_DEFAULT_LOCALE", "en")
AVAILABLE_LOCALES = [l.strip() for l in os.getenv("LH_LOCALES", "en,zh").split(",") if l.strip()]

# Public base URL for canonical/Open Graph tags (empty => tags render relative paths)
BASE_URL = os.getenv("LH_BASE_URL", "").rstrip("/")

# Scholar six-dimension portrait keys (canonical order)
TRAIT_KEYS = ["taste", "quality", "spirit", "character", "concerns", "philosophy"]

# Source quality grades, per PRINCIPLES.md (A=primary, D=unverified)
SOURCE_LEVELS = ["A", "B", "C", "D"]

# Admin console bearer token; admin routes stay closed when unset/empty
ADMIN_TOKEN = os.getenv("LH_ADMIN_TOKEN", "")

# Paths
TEMPLATE_DIR = Path(__file__).parent / "templates"
STATIC_DIR = Path(__file__).parent / "static"
DATA_DIR = BASE_DIR / "data"