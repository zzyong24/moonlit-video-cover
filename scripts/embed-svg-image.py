#!/usr/bin/env python3
"""Embed one raster evidence image into a cover SVG before export."""

from __future__ import annotations

import argparse
import base64
import mimetypes
from pathlib import Path


TOKEN = "__EVIDENCE_DATA_URI__"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--svg", required=True, type=Path)
    parser.add_argument("--image", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    svg = args.svg.read_text(encoding="utf-8")
    if TOKEN not in svg:
        raise SystemExit(f"missing token {TOKEN} in {args.svg}")

    mime = mimetypes.guess_type(args.image.name)[0] or "application/octet-stream"
    payload = base64.b64encode(args.image.read_bytes()).decode("ascii")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        svg.replace(TOKEN, f"data:{mime};base64,{payload}"), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
