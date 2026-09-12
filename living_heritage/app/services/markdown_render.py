"""
Markdown -> safe HTML rendering.

Canonical note bodies are stored as raw Markdown (LaTeX kept inline in $ $
/ $$ $$) inside bilingual_text; rendering happens at read time. LaTeX is
rendered client-side by KaTeX (local static assets, no CDN).
"""
import re

import markdown as md_lib

_MD = md_lib.Markdown(
    extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
    output_format="html5",
    tab_length=4,
)


def render_markdown(text: str) -> str:
    """Render Markdown to HTML, preserving raw HTML as-is (admin-authored content)."""
    if not text:
        return ""
    return _MD.convert(text)


def contains_latex(text: str) -> bool:
    """Heuristic: does the text contain TeX delimiters for KaTeX auto-render?"""
    if not text:
        return False
    return bool(re.search(r"(?<!\$)\$(?!\$)[^$]+\$|\$\$", text))