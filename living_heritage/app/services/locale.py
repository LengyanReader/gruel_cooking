"""
Bilingual text resolution — single source of i18n logic.
All user-facing strings flow through resolve_text().
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
