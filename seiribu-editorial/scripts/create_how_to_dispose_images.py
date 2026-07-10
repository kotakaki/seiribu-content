#!/usr/bin/env python3
"""Render finished article images for the how-to-dispose article."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "images" / "how-to-dispose"
RENDERER = ROOT / "scripts" / "render_how_to_dispose_images.mjs"
BUNDLED_NODE = (
    Path.home()
    / ".cache"
    / "codex-runtimes"
    / "codex-primary-runtime"
    / "dependencies"
    / "node"
    / "bin"
    / "node"
)


def node_executable() -> str:
    if BUNDLED_NODE.exists():
        return str(BUNDLED_NODE)
    node = shutil.which("node")
    if not node:
        raise RuntimeError("Node.js is required to render the article images.")
    return node


def convert_eyecatch_to_webp() -> Path:
    png = OUT_DIR / "how-to-dispose-eyecatch.png"
    webp = OUT_DIR / "how-to-dispose-eyecatch.webp"
    if not png.exists():
        raise FileNotFoundError(f"Renderer did not produce {png}")
    Image.open(png).convert("RGB").save(webp, quality=92, method=6)
    return webp


def main() -> None:
    subprocess.run([node_executable(), str(RENDERER)], check=True)
    webp = convert_eyecatch_to_webp()
    print(f"Wrote {webp}")


if __name__ == "__main__":
    main()
