"""Command line interface for generating quick musical ideas."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Optional, Sequence

from .composer import create_song


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a small musical sketch")
    parser.add_argument("--key", default="C", help="Key of the song (default: C)")
    parser.add_argument(
        "--mode",
        default="major",
        help="Scale mode to use. Supported values: major, minor, dorian, mixolydian",
    )
    parser.add_argument("--bars", type=int, default=4, help="Number of bars to generate")
    parser.add_argument(
        "--beats-per-bar",
        dest="beats_per_bar",
        type=int,
        default=4,
        help="Beats per bar (default: 4)",
    )
    parser.add_argument(
        "--progression",
        nargs="+",
        type=int,
        help="Space separated chord degrees, e.g. --progression 1 5 6 4",
    )
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible output")
    parser.add_argument("--no-rests", action="store_true", help="Disable rests in the generated melody")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional path to write the generated song as JSON",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    song = create_song(
        key=args.key,
        mode=args.mode,
        bars=args.bars,
        beats_per_bar=args.beats_per_bar,
        progression=args.progression,
        allow_rests=not args.no_rests,
        seed=args.seed,
    )

    payload = json.dumps(song, indent=2)
    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)

    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
