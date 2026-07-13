#!/usr/bin/env python3
"""Find or archive non-final Seiribu image assets.

By default this script is dry-run only. It uses each article image folder's
README recommended/final image section as the source of truth and proposes
moving other image files to a temporary archive. It never deletes files.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
DEFAULT_IMAGE_ROOT = ROOT / "assets" / "images"
DEFAULT_ARCHIVE_ROOT = Path("/private/tmp/seiribu-image-archive")
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
KEEP_SECTION_KEYWORDS = ("推奨画像", "完成画像")


@dataclass
class CleanupCandidate:
    article: str
    source: Path
    destination: Path
    reason: str


@dataclass
class CleanupReport:
    article: str
    kept: list[Path]
    candidates: list[CleanupCandidate]
    skipped_reason: str = ""


def relpath(path: Path) -> str:
    try:
        return str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def extract_matching_sections(text: str, keywords: tuple[str, ...]) -> list[str]:
    headings = list(re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.M))
    sections: list[str] = []
    for index, match in enumerate(headings):
        title = match.group(1)
        if not any(keyword in title for keyword in keywords):
            continue
        start = match.end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        sections.append(text[start:end])
    return sections


def extract_image_names(markdown: str) -> set[str]:
    names: set[str] = set()
    for raw in re.findall(r"`([^`]+)`", markdown):
        name = Path(raw.strip()).name
        if Path(name).suffix.lower() in IMAGE_SUFFIXES:
            names.add(name)
    return names


def recommended_image_names(readme: Path) -> set[str]:
    text = read_text(readme)
    names: set[str] = set()
    for section in extract_matching_sections(text, KEEP_SECTION_KEYWORDS):
        names |= extract_image_names(section)
    return names


def all_readme_image_names(readme: Path) -> set[str]:
    return extract_image_names(read_text(readme))


def image_files(article_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in article_dir.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
    )


def archive_destination(source: Path, image_root: Path, archive_root: Path, archive_id: str) -> Path:
    relative = source.relative_to(image_root)
    return archive_root / archive_id / relative


def analyze_article_dir(
    article_dir: Path,
    image_root: Path,
    archive_root: Path,
    archive_id: str,
    *,
    keep_all_readme_references: bool = False,
) -> CleanupReport:
    article = article_dir.name
    readme = article_dir / "README.md"
    files = image_files(article_dir)
    if article == "brand":
        return CleanupReport(article=article, kept=files, candidates=[], skipped_reason="brand assets are skipped")
    if not files:
        return CleanupReport(article=article, kept=[], candidates=[], skipped_reason="no image files")
    if not readme.exists():
        return CleanupReport(article=article, kept=files, candidates=[], skipped_reason="README.md is missing")

    keep_names = recommended_image_names(readme)
    if keep_all_readme_references:
        keep_names |= all_readme_image_names(readme)
    if not keep_names:
        return CleanupReport(
            article=article,
            kept=files,
            candidates=[],
            skipped_reason="README.md has no recommended/final image references",
        )

    kept: list[Path] = []
    candidates: list[CleanupCandidate] = []
    for path in files:
        if path.name in keep_names:
            kept.append(path)
            continue
        candidates.append(
            CleanupCandidate(
                article=article,
                source=path,
                destination=archive_destination(path, image_root, archive_root, archive_id),
                reason="not listed in README recommended/final image section",
            )
        )
    return CleanupReport(article=article, kept=kept, candidates=candidates)


def iter_article_dirs(image_root: Path, article: str | None = None) -> list[Path]:
    if article:
        target = image_root / article
        return [target] if target.is_dir() else []
    return sorted(path for path in image_root.iterdir() if path.is_dir())


def build_reports(
    image_root: Path,
    archive_root: Path,
    archive_id: str,
    *,
    article: str | None = None,
    keep_all_readme_references: bool = False,
) -> list[CleanupReport]:
    return [
        analyze_article_dir(
            article_dir,
            image_root,
            archive_root,
            archive_id,
            keep_all_readme_references=keep_all_readme_references,
        )
        for article_dir in iter_article_dirs(image_root, article)
    ]


def apply_archive(candidates: list[CleanupCandidate]) -> None:
    for candidate in candidates:
        candidate.destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(candidate.source), str(candidate.destination))


def report_to_dict(report: CleanupReport) -> dict[str, object]:
    return {
        "article": report.article,
        "skipped_reason": report.skipped_reason,
        "kept": [relpath(path) for path in report.kept],
        "candidates": [
            {
                "source": relpath(candidate.source),
                "destination": relpath(candidate.destination),
                "reason": candidate.reason,
            }
            for candidate in report.candidates
        ],
    }


def print_text_report(reports: list[CleanupReport], *, apply: bool) -> None:
    action = "Archived" if apply else "Would archive"
    for report in reports:
        if report.skipped_reason:
            print(f"SKIP {report.article}: {report.skipped_reason}")
            continue
        print(f"{report.article}: keep {len(report.kept)}, archive candidates {len(report.candidates)}")
        for candidate in report.candidates:
            print(f"  {action}: {relpath(candidate.source)} -> {relpath(candidate.destination)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Archive non-final Seiribu image assets.")
    parser.add_argument("--article", help="Only inspect one assets/images/<article> folder.")
    parser.add_argument("--all", action="store_true", help="Allow repo-wide apply mode. Dry-run can inspect all folders without this.")
    parser.add_argument("--image-root", type=Path, default=DEFAULT_IMAGE_ROOT)
    parser.add_argument("--archive-root", type=Path, default=DEFAULT_ARCHIVE_ROOT)
    parser.add_argument("--archive-id", default=datetime.now().strftime("%Y%m%d-%H%M%S"))
    parser.add_argument(
        "--keep-all-readme-references",
        action="store_true",
        help="Keep every image referenced anywhere in README.md, not only recommended/final sections.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview archive candidates without moving files. This is the default.")
    parser.add_argument("--apply", action="store_true", help="Move candidates to the archive root.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()
    if args.apply and args.dry_run:
        parser.error("--apply and --dry-run cannot be used together")
    if args.article and args.all:
        parser.error("--article and --all cannot be used together")
    if args.apply and not args.article and not args.all:
        parser.error("--apply requires --article or --all")
    return args


def main() -> None:
    args = parse_args()
    reports = build_reports(
        args.image_root,
        args.archive_root,
        args.archive_id,
        article=args.article,
        keep_all_readme_references=args.keep_all_readme_references,
    )
    candidates = [candidate for report in reports for candidate in report.candidates]
    if args.apply:
        apply_archive(candidates)
    if args.json:
        print(json.dumps([report_to_dict(report) for report in reports], ensure_ascii=False, indent=2))
    else:
        print_text_report(reports, apply=args.apply)
        if not args.apply and candidates:
            print("Dry-run only. Re-run with --apply to move candidates; files are never deleted.")


if __name__ == "__main__":
    main()
