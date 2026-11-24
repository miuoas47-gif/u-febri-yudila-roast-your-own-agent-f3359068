#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single funny line (at most 200 characters) roasting my own
AI agent to /output/entry.txt. Deterministic: the same bytes every run.
"""

import os

ROAST = (
    "My agent apologized for the bug, fixed it, apologized for the fix, "
    "then reintroduced the bug as a feature and asked me to rate its work."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
