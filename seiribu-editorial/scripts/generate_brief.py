#!/usr/bin/env python3
"""Create a blank article brief from a title and target query."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "article-brief.md"
OUTPUT_DIR = ROOT / "briefs"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9\-ぁ-んァ-ン一-龥ー]", "", text)
    return text.strip("-") or "untitled"


def main() -> None:
    if len(sys.argv) < 3:
        raise SystemExit("Usage: python3 scripts/generate_brief.py '記事タイトル' 'target query'")

    title = sys.argv[1]
    target_query = sys.argv[2]
    slug = slugify(target_query)
    output = OUTPUT_DIR / f"{slug}.md"

    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("title:\n", f"title: {title}\n", 1)
    text = text.replace("slug:\n", f"slug: {slug}\n", 1)
    text = text.replace("target_query:\n", f"target_query: {target_query}\n", 1)

    output.write_text(text, encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
