"""
Configuration — all from environment, nothing hardcoded.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# SQLite
SQLITE_PATH = os.getenv("LH_SQLITE_PATH", str(BASE_DIR / "data" / "living_heritage.db"))

# Neo4j
NEO4J_URI = os.getenv("LH_NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("LH_NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("LH_NEO4J_PASSWORD", "")

# Locale
DEFAULT_LOCALE = os.getenv("LH_DEFAULT_LOCALE", "en")
AVAILABLE_LOCALES = ["en", "zh"]

# Paths
TEMPLATE_DIR = Path(__file__).parent / "templates"
STATIC_DIR = Path(__file__).parent / "static"
DATA_DIR = BASE_DIR / "data"
