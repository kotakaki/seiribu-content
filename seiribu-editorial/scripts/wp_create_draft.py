#!/usr/bin/env python3
"""Placeholder for WordPress draft creation.

This script intentionally does not publish posts. Add WordPress credentials and
API code only after the human review flow is confirmed.
"""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 scripts/wp_create_draft.py reviewed/article.md")

    path = Path(sys.argv[1])
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    text = path.read_text(encoding="utf-8")
    if "human_review_required: true" not in text:
        raise SystemExit("Refusing to continue: human_review_required: true is missing.")

    print("WordPress draft creation is not configured yet.")
    print("This script will only create drafts after credentials and review policy are added.")


if __name__ == "__main__":
    main()
