#!/usr/bin/env python3
"""Suggest internal links for a draft from strategy/internal-link-map.md."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK_MAP = ROOT / "strategy" / "internal-link-map.md"


KEYWORDS = {
    "実家の片付けで売れるもの一覧": ["売れるもの", "実家", "片付け"],
    "買取基準に満たないと言われた理由": ["買取基準", "買取不可", "売れにくい"],
    "実家の不用品は買取と回収どちらが先？": ["回収", "処分", "不用品"],
    "買取不可だったものを処分する方法": ["買取不可", "処分方法", "自治体"],
}


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 scripts/build_internal_links.py drafts/article.md")

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    suggestions: list[str] = []

    for title, words in KEYWORDS.items():
        if title in text:
            continue
        hits = [word for word in words if re.search(re.escape(word), text)]
        if hits:
            suggestions.append(f"- {title}: 関連語 {', '.join(hits)} が本文にあります")

    if not suggestions:
        print("内部リンク候補は見つかりませんでした。")
        return

    print("内部リンク候補:")
    print("\n".join(suggestions))


if __name__ == "__main__":
    main()
