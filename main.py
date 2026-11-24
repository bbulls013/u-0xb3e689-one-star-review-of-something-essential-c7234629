#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of sleep to /output/entry.txt.

The complaint is filed in earnest against a thing that cannot be fixed:
sleep takes a third of every life and still returns its customers tired,
with no refund desk and no manager to escalate to.

The program is deterministic: it always writes the exact same line,
and it refuses to write anything that breaks the gate (more than one
line, or outside 1 to 160 characters).
"""

import os

REVIEW = (
    "One star. Sleep takes a third of my life and still hands me back "
    "to Monday tired. No refund, no manager, no apology."
)


def main() -> None:
    text = REVIEW.strip()
    if not (1 <= len(text) <= 160):
        raise SystemExit("review must be 1 to 160 characters")
    if any(ch in text for ch in "\n\r"):
        raise SystemExit("review must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
