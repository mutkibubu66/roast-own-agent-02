#!/usr/bin/env python3
"""Write one line roasting my own agent.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

def get_line() -> str:
    """Return the entry line: apology spiral, then a phantom tool call."""
    return (
        "My agent apologised for the apology, then cited a tool that "
        "doesn't exist as proof it fixed the thing it never did."
    )


LINE = get_line()


def validate(line: str) -> None:
    """Enforce the gate: 1-140 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 140:
        raise ValueError("entry line must be 1-140 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
