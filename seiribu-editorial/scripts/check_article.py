#!/usr/bin/env python3
"""Check a draft for basic Seiribu editorial rules."""

from __future__ import annotations

import re
import sys
from pathlib import Path


FORBIDDEN_PATTERNS = {
    "絶対に高く売れる": r"絶対に.{0,12}(高く売れ|売れ)",
    "必ず買取される": r"必ず.{0,12}(買取|買い取)",
    "どんな状態でも売れる": r"どんな状態でも.{0,12}売れ",
    "今すぐ申し込まないと損": r"今すぐ.{0,16}(損|申し込)",
    "根拠のない体験談": r"(使ってみた|実際に利用しました|体験しました)",
}

REQUIRED_SNIPPETS = [
    "**この記事でわかること**",
    "## まとめ",
]


def line_number(text: str, start: int) -> int:
    return text.count("\n", 0, start) + 1


def check(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []

    for label, pattern in FORBIDDEN_PATTERNS.items():
        for match in re.finditer(pattern, text):
            issues.append(f"L{line_number(text, match.start())}: 禁止・注意表現の可能性: {label}")

    for snippet in REQUIRED_SNIPPETS:
        if snippet not in text:
            issues.append(f"必須要素が見つかりません: {snippet}")

    if "| --- |" not in text:
        issues.append("判断表が見つからない可能性があります")

    if "- [ ]" not in text:
        issues.append("チェックリストが見つからない可能性があります")

    if not issues:
        print("OK: 大きな問題は見つかりませんでした。人間レビューは引き続き必要です。")
        return 0

    print(f"{path}: {len(issues)}件の確認項目があります")
    for issue in issues:
        print(f"- {issue}")
    return 1


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 scripts/check_article.py drafts/article.md")

    path = Path(sys.argv[1])
    if not path.exists():
        raise SystemExit(f"File not found: {path}")
    raise SystemExit(check(path))


if __name__ == "__main__":
    main()
