"""
prune_outputs.py -- Keep only the N most-recent dated post folders per type, delete older ones.

Folders are named `YYYY-MM-DD_topic-slug/` (lexicographic sort = chronological sort).
Only folders matching that pattern are considered for pruning. Folders without a date
prefix (e.g. historical pre-migration outputs, Favoritos folder) are NEVER touched.

Usage:
    python Brand/prune_outputs.py <type> [max_keep]

    type      one of: step-by-step, news, informativos, all
    max_keep  default 5

Examples:
    python Brand/prune_outputs.py news            # keep last 5 in PostTypes/news/Outputs/
    python Brand/prune_outputs.py all 5           # prune all 3 types to last 5
    python Brand/prune_outputs.py informativos 3  # keep only 3 most recent informativos

This script is idempotent and safe to call after every post creation.
"""
import os
import re
import shutil
import sys
from pathlib import Path

DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}_")
VALID_TYPES = ("step-by-step", "news", "informativos")
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def prune_one(post_type: str, max_keep: int = 5) -> None:
    if post_type not in VALID_TYPES:
        raise ValueError(f"Unknown post_type: {post_type}. Must be one of {VALID_TYPES}")

    outputs_dir = PROJECT_ROOT / "PostTypes" / post_type / "Outputs"
    if not outputs_dir.is_dir():
        print(f"[{post_type}] Outputs dir does not exist: {outputs_dir}")
        return

    # Collect dated folders only (folders whose name starts with YYYY-MM-DD_)
    dated = [
        d for d in outputs_dir.iterdir()
        if d.is_dir() and DATE_PATTERN.match(d.name)
    ]
    # Sort descending by name (= descending by date, then alphabetical within same day)
    dated.sort(key=lambda d: d.name, reverse=True)

    keep = dated[:max_keep]
    remove = dated[max_keep:]

    print(f"[{post_type}] {len(dated)} dated folder(s) found, keeping {len(keep)}, removing {len(remove)}")
    for d in keep:
        print(f"  KEEP    {d.name}")
    for d in remove:
        print(f"  DELETE  {d.name}")
        shutil.rmtree(d)


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    post_type = sys.argv[1]
    max_keep = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    if post_type == "all":
        for t in VALID_TYPES:
            prune_one(t, max_keep)
    else:
        prune_one(post_type, max_keep)


if __name__ == "__main__":
    main()
