#!/usr/bin/env python3
"""Score Search Console query CSV rows and write an opportunity report."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "search-console" / "queries.csv"
OUTPUT = ROOT / "reports" / "keyword-opportunities.md"


@dataclass
class Keyword:
    query: str
    clicks: float
    impressions: float
    ctr: float
    position: float

    @property
    def score(self) -> float:
        position_gap = max(0.0, 15.0 - self.position)
        ctr_gap = max(0.0, 0.08 - self.ctr) * 100
        return (self.impressions * 0.5) + (position_gap * 30) + ctr_gap - (self.clicks * 0.2)


def as_float(value: str) -> float:
    value = (value or "").replace("%", "").replace(",", "").strip()
    if not value:
        return 0.0
    number = float(value)
    if number > 1 and "%" in value:
        return number / 100
    return number


def pick(row: dict[str, str], *names: str) -> str:
    normalized = {key.lower().strip(): value for key, value in row.items()}
    for name in names:
        if name.lower() in normalized:
            return normalized[name.lower()]
    return ""


def load_keywords() -> list[Keyword]:
    if not INPUT.exists():
        raise SystemExit(f"Missing input file: {INPUT}")

    with INPUT.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        keywords = []
        for row in reader:
            query = pick(row, "query", "queries", "検索キーワード", "検索語句")
            if not query:
                continue
            keywords.append(
                Keyword(
                    query=query,
                    clicks=as_float(pick(row, "clicks", "クリック数")),
                    impressions=as_float(pick(row, "impressions", "表示回数")),
                    ctr=as_float(pick(row, "ctr", "平均CTR")),
                    position=as_float(pick(row, "position", "average position", "掲載順位")),
                )
            )
    return keywords


def main() -> None:
    keywords = sorted(load_keywords(), key=lambda item: item.score, reverse=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# キーワード機会レポート",
        "",
        "| 優先度 | クエリ | Clicks | Impressions | CTR | Position | Memo |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]

    for keyword in keywords[:50]:
        priority = "high" if keyword.score >= 500 else "medium" if keyword.score >= 150 else "low"
        lines.append(
            f"| {priority} | {keyword.query} | {keyword.clicks:.0f} | "
            f"{keyword.impressions:.0f} | {keyword.ctr:.2%} | {keyword.position:.1f} |  |"
        )

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
