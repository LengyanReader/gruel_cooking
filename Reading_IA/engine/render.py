# -*- coding: utf-8 -*-
"""engine/render.py — RKF L4 presentation engine (thin, registry-driven).

This is the "render engine" half of the split: it holds NO domain constants.
Every visual fact is read from ``knowledge/`` registries:

  styles.css            the shared stylesheet (was an inline CSS string)
  script.js             the language-toggle script (was inline)
  graph/schema.json     node/edge labels + colors + dash + confidence marks
  page_spec/<kind>.json per-kind section order + the chapter-brief labels
  templates/*.html      {{token}} partials (brief_block.html reproduces the
                        per-chapter lossless brief box in eb59bf4)

`web/build_reading.py` imports this module and asks it for those values, so the
monolith no longer hard-codes CSS/EDGE_KIND/CONF_COLOR/dash/section-labels —
adding a relation type or re-theming is a data edit, not a Python edit.

The renderer supports a documented template subset:
  {{key}}                     simple substitution (value is used verbatim — the
                              caller HTML-escapes before it hands strings over)
  {{#list}} ... {{/list}}     repeat the block once per dict in ctx["list"]
Nothing else; it is deliberately ~40 lines (locked assumption A2: no Jinja).
"""
from __future__ import annotations

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE = os.path.normpath(os.path.join(HERE, "..", "knowledge"))
TEMPLATES = os.path.join(KNOWLEDGE, "templates")
PAGE_SPEC = os.path.join(KNOWLEDGE, "page_spec")


def read(relpath: str) -> str:
    with open(os.path.join(KNOWLEDGE, relpath), encoding="utf-8") as fh:
        return fh.read()


def load_json(relpath: str):
    with open(os.path.join(KNOWLEDGE, relpath), encoding="utf-8") as fh:
        return json.load(fh)


def styles() -> str:
    return read("styles.css")


def script() -> str:
    return read("script.js")


def graph_schema() -> dict:
    return load_json(os.path.join("graph", "schema.json"))


def page_spec(kind: str) -> dict:
    path = os.path.join(PAGE_SPEC, f"{kind}.json")
    if not os.path.exists(path):  # fall back to generic
        path = os.path.join(PAGE_SPEC, "generic.json")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_template(name: str) -> str:
    with open(os.path.join(TEMPLATES, name), encoding="utf-8") as fh:
        return fh.read()


# ---- derived, schema-driven constant maps (replace build_reading literals) ----
def edge_kind_map(schema: dict) -> dict:
    """kind -> (bilingual label, color) — the successor of hard-coded EDGE_KIND."""
    return {k: (v.get("label_zh", k), v.get("color", "#8C8C8C"))
            for k, v in schema.get("edge_types", {}).items()}


def edge_dash_map(schema: dict) -> dict:
    """kind -> svg dasharray, straight from the edge registry."""
    return {k: v.get("dash", "1") for k, v in schema.get("edge_types", {}).items()}


def conf_color_map(schema: dict) -> dict:
    """confidence mark -> color — the successor of hard-coded CONF_COLOR."""
    return dict(schema.get("confidence", {}).get("marks", {}))


# ---- tiny {{token}} / {{#list}} renderer ----
_SECTION_RE = re.compile(r"\{\{#(\w+)\}\}(.*?)\{\{/\1\}\}", re.S)
_TOKEN_RE = re.compile(r"\{\{(\w+)\}\}")


def _subst(text: str, ctx: dict) -> str:
    return _TOKEN_RE.sub(lambda m: str(ctx.get(m.group(1), "")), text)


def render(template: str, ctx: dict) -> str:
    """Expand {{#list}}...{{/list}} (repeat per dict item) then {{token}}."""
    def _expand(m):
        key, body = m.group(1), m.group(2)
        items = ctx.get(key) or []
        return "".join(_subst(body, it if isinstance(it, dict) else {".": it}) for it in items)

    out = _SECTION_RE.sub(_expand, template)
    return _subst(out, ctx)


def brief_html(block: dict, labels: list, brief: dict) -> str:
    """Render a per-chapter lossless brief box from a template + label registry.
    `labels` is [[key, zh, en], ...]; zh text comes from ``brief[key]`` and the
    English side from ``brief[key + '_en']``, falling back to the zh text when
    the English has not been authored yet (graceful degradation). Only rows with
    any content are shown; values are HTML-escaped here so the template stays
    pure structure."""
    import html as _html
    rows = []
    for key, zh_lab, en_lab in labels:
        zh = (brief.get(key) or "").strip()
        en = (brief.get(key + "_en") or "").strip() or zh
        if not zh and not en:
            continue
        rows.append({"zh_lab": _html.escape(zh_lab), "en_lab": _html.escape(en_lab),
                     "txt_zh": _html.escape(zh), "txt_en": _html.escape(en)})
    if not rows:
        return ""
    tpl = load_template(block["template"])
    return render(tpl, {"rows": rows})
