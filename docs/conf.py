"""Sphinx configuration derived from the authoritative manuscript."""

from __future__ import annotations

import re
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = REPOSITORY_ROOT / "manuscript" / "knot_fewnomials.tex"
MANUSCRIPT_TEXT = MANUSCRIPT.read_text(encoding="utf-8")


def manuscript_field(command: str) -> str:
    """Read a simple, single-line ``\\command{...}`` field from the paper."""
    match = re.search(rf"^\\{command}\{{([^{{}}]+)\}}$", MANUSCRIPT_TEXT, re.MULTILINE)
    if match is None:
        raise RuntimeError(f"Could not read \\{command} from {MANUSCRIPT}")
    return match.group(1).replace(r"\and", " and ")


paper_title = manuscript_field("title")
paper_authors = manuscript_field("author")

project = paper_title
author = paper_authors
copyright = f"2026, {paper_authors}"
release = "0.1.0"

extensions = ["sphinx.ext.mathjax"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "alabaster"
html_title = f"{paper_title} — documentation"

# These files are copied from their authoritative location into the HTML root.
# The documentation tree deliberately contains no duplicate manuscript.
html_extra_path = [
    "../manuscript/knot_fewnomials.pdf",
    "../manuscript/knot_fewnomials.tex",
    "../ACKNOWLEDGMENTS.md",
    "../FORMAL_VERIFICATION.md",
    "../NOVELTY_AUDIT.md",
    "../REPRODUCIBILITY.md",
]

mathjax3_config = {
    "tex": {
        "inlineMath": [[r"\(", r"\)"]],
        "displayMath": [[r"\[", r"\]"]],
    }
}
