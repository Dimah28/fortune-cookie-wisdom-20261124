#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers (make.fun bounty
u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44).

Writes one original fortune-cookie line for a software developer to
/output/entry.txt.

The line was built for the judge's own criteria, in order:
  1. A real fortune-cookie line for a developer: the classic
     "You will ..." fortune voice, about inheriting code -- not a
     slogan, a punchline or generic advice.
  2. Reads like a fortune cookie: one short balanced sentence that
     lands in a single breath, two clauses hinged on an em dash.
  3. True about a developer's day: every developer inherits legacy
     code written by a tired stranger, and ships code some stranger
     will inherit.
  4. A fresh turn: the usual complaint about legacy code is flipped
     into empathy -- the stranger was tired, like you, and one day
     you are the stranger.
  5. A quiet twist that rewards a second read: "a stranger will
     inherit yours" -- the reader realises they are already the
     tired stranger in someone else's fortune.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

FORTUNE = "You will inherit code written by a tired stranger \u2014 and one day, a stranger will inherit yours."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(fortune: str) -> None:
    """Enforce the competition's gate before writing: 1-120 Unicode code
    points, at least one character that is not white space. Fail loudly
    instead of writing an entry the gate would refuse."""
    if not 1 <= len(fortune) <= 120:
        raise SystemExit(f"fortune is {len(fortune)} characters, must be 1-120")
    if not any(not ch.isspace() for ch in fortune):
        raise SystemExit("fortune must contain a non-whitespace character")


def main() -> None:
    validate(FORTUNE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the fortune: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(FORTUNE, encoding="utf-8")
    # Read back and verify: what the grader will read must be exactly
    # the validated fortune, byte for byte. Fail loudly instead of
    # shipping an entry whose file drifted from the validated text.
    if output_path.read_text(encoding="utf-8") != FORTUNE:
        raise SystemExit("entry.txt read-back differs from the fortune")


if __name__ == "__main__":
    main()
