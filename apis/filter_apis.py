#!/usr/bin/env python3
"""Filter the open API library by topic, auth, or keyword.

The library lives as Markdown tables in this directory (one file per topic), with columns:
    | API | Description | Auth | HTTPS | Docs |

This script parses every `*.md` table and lets you filter across all of them.

Examples:
    python filter_apis.py                        # list everything
    python filter_apis.py --no-auth              # only APIs that need no key
    python filter_apis.py --topic weather        # only the weather topic
    python filter_apis.py --search crypto        # match name/description/topic
    python filter_apis.py --auth apiKey          # only apiKey APIs
    python filter_apis.py --search image --json  # JSON output for piping

No third-party dependencies — standard library only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKIP_FILES = {"README.md"}


def parse_file(path: Path) -> list[dict]:
    """Extract API rows from a topic Markdown file."""
    topic = path.stem
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5:
            continue
        name = cells[0]
        # Skip header and separator rows.
        if name.lower() == "api" or set(name) <= {"-", ":"}:
            continue
        rows.append(
            {
                "topic": topic,
                "api": name,
                "description": cells[1],
                "auth": cells[2],
                "https": cells[3],
                "docs": _extract_url(cells[4]),
            }
        )
    return rows


def _extract_url(cell: str) -> str:
    m = re.search(r"\((https?://[^)]+)\)", cell)  # markdown link
    if m:
        return m.group(1)
    m = re.search(r"https?://\S+", cell)  # bare url
    return m.group(0) if m else cell


def load_all() -> list[dict]:
    rows: list[dict] = []
    for path in sorted(HERE.glob("*.md")):
        if path.name in SKIP_FILES:
            continue
        rows.extend(parse_file(path))
    return rows


def matches(row: dict, args: argparse.Namespace) -> bool:
    if args.topic and args.topic.lower() not in row["topic"].lower():
        return False
    if args.auth and args.auth.lower() not in row["auth"].lower():
        return False
    if args.no_auth and not row["auth"].lower().startswith("no"):
        return False
    if args.search:
        hay = f"{row['api']} {row['description']} {row['topic']}".lower()
        if args.search.lower() not in hay:
            return False
    return True


def main() -> int:
    p = argparse.ArgumentParser(description="Filter the open API library.")
    p.add_argument("--topic", help="filter by topic (file name), e.g. weather")
    p.add_argument("--auth", help="filter by auth type substring, e.g. apiKey, OAuth, token")
    p.add_argument("--no-auth", action="store_true", help="only APIs that need no auth")
    p.add_argument("--search", help="keyword match on name/description/topic")
    p.add_argument("--json", action="store_true", help="output JSON")
    args = p.parse_args()

    rows = [r for r in load_all() if matches(r, args)]
    rows.sort(key=lambda r: (r["topic"], r["api"].lower()))

    if args.json:
        json.dump(rows, sys.stdout, indent=2, ensure_ascii=False)
        print()
        return 0

    if not rows:
        print("No APIs matched.")
        return 1

    width = max(len(r["api"]) for r in rows)
    current = None
    for r in rows:
        if r["topic"] != current:
            current = r["topic"]
            print(f"\n== {current} ==")
        print(f"  {r['api']:<{width}}  [{r['auth']}]  {r['docs']}")
    print(f"\n{len(rows)} APIs.")
    return 0


if __name__ == "__main__":
    try:
        # Restore default SIGPIPE so piping into `head` etc. exits quietly (POSIX only).
        import signal

        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        raise SystemExit(0)
