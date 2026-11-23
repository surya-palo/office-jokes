#!/usr/bin/env python3
"""Writes the office-joke entry to /output/entry.txt.

Stdlib only. Deterministic: the joke is a constant, so every run
produces byte-identical output.
"""

from pathlib import Path

JOKE = "My boss said AI could never replace me — then asked me to train my replacement."

def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
