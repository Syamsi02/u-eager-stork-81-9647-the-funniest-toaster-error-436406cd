#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one line -- the error message a kitchen toaster shows its owner --
to /output/entry.txt. Pure standard library, fully deterministic: the same
line on every run.
"""

import sys
from pathlib import Path

# The entry: a deadpan appliance error code, then the bread quitting the
# job in the language of a showbiz split. No toaster pun, no setup that
# needs a second sentence.
LINE = "E03: BREAD DECLINED TO BROWN. IT CITES CREATIVE DIFFERENCES."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> int:
    if not 1 <= len(LINE) <= 120:
        print(f"entry is {len(LINE)} characters, must be 1-120", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    # Read back and confirm the file holds exactly the line, no trailing
    # newline and no extra bytes, so the graded artifact is byte-identical
    # to the line above on every run.
    if OUTPUT_PATH.read_text(encoding="utf-8") != LINE:
        print("read-back mismatch on entry.txt", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
