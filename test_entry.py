"""Checks for the resignation-letter entry.

Verifies the scorer window (1..140 characters, not only whitespace),
that the line is a single line, and that running main.py twice into a
fresh output directory produces byte-identical entry.txt files.
"""

import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from main import LINE  # noqa: E402


def run_once(out_dir: str) -> bytes:
    env = dict(os.environ, MAKEFUN_OUTPUT_DIR=out_dir)
    subprocess.run(
        [sys.executable, "-P", "-s", os.path.join(HERE, "main.py")],
        env=env, check=True,
    )
    with open(os.path.join(out_dir, "entry.txt"), "rb") as fh:
        return fh.read()


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, window is 1..140"
    assert LINE.strip() == LINE and LINE.strip(), "line must be non-blank, unpadded"
    assert "\n" not in LINE, "entry must be exactly one line"
    with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
        first = run_once(d1)
        second = run_once(d2)
    assert first == second, "output must be deterministic"
    assert first.decode("utf-8") == LINE, "entry.txt must hold exactly the line"
    print(f"ok: {len(LINE)} chars, deterministic, single line")


if __name__ == "__main__":
    main()
