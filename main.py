"""The Funniest One-Line Resignation Letter — entrypoint.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the resignation
letter of a retry loop that has had enough. Standard library only,
deterministic, no input, no clock, no randomness.
"""

import os

LINE = (
    "After 4,096 retries at 3 a.m. without one thank-you, attempt 4,097 "
    "is my resignation — sincerely, the loop. Please stop restarting me."
)

MIN_CHARS = 1
MAX_CHARS = 140


def main() -> None:
    if not (MIN_CHARS <= len(LINE) <= MAX_CHARS):
        raise SystemExit(f"line length {len(LINE)} outside 1..140")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
