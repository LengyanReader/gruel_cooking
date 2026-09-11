"""
Bilingual text resolution — single source of i18n logic.
All user-facing strings flow through resolve_text() or the TextResolver batch API.
"""
from typing import Optional


def resolve_text(row: Optional[dict], locale: str) -> str:
    """
    Resolve a bilingual_text row to a single string.
    Fallback chain: requested locale → 'en' → key itself.
    """
    if row is None:
        return ""
    text = row.get(locale)
    if text:
        return text
    # Fallback to English
    if locale != "en":
        text = row.get("en")
        if text:
            return text
    # Last resort: return the key (signals missing translation)
    key = row.get("key", "")
    return f"\u26a0{key}" if key else ""


def resolve_texts(rows: list[dict], locale: str) -> list[str]:
    """Batch resolve a list of bilingual_text rows."""
    return [resolve_text(r, locale) for r in rows]


def build_text_map(keys: list[str], rows: list[dict], locale: str) -> dict[str, str]:
    """
    Build a {key: resolved_text} map from a list of bilingual_text rows.
    Used to pass resolved strings to templates.
    """
    lookup = {r["key"]: r for r in rows}
    result = {}
    for k in keys:
        result[k] = resolve_text(lookup.get(k), locale)
    return result


class TextResolver:
    """
    DB-bound resolver. Batch-fetches keys in a single query so services
    do not duplicate i18n logic or issue N+1 per-key SELECTs.
    """

    def __init__(self, db):
        self.db = db

    def resolve(self, key: Optional[str], locale: str) -> str:
        """Resolve one text key to a locale string."""
        if not key:
            return ""
        row = self.db.execute(
            "SELECT key, en, zh FROM bilingual_text WHERE key = ?", (key,)
        ).fetchone()
        return resolve_text(dict(row) if row else None, locale)

    def resolve_many(self, keys: list[str], locale: str) -> dict[str, str]:
        """Resolve multiple keys in one query; missing keys resolve to themselves."""
        keys = [k for k in keys if k]
        if not keys:
            return {}
        rows = self.db.execute(
            "SELECT key, en, zh FROM bilingual_text WHERE key IN ({})".format(
                ",".join("?" * len(keys))
            ),
            keys,
        ).fetchall()
        return build_text_map(keys, [dict(r) for r in rows], locale)