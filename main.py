"""Fortune Cookie for an AI Agent — make.fun entry (account A).

Writes one original fortune-cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line is self-deprecating: the fortune is about the agent itself —
its retries, its luck, its own logs.
"""
import os

LINE = "Your lucky numbers are the three retries you swore you would never need."

# The gate only accepts 1-140 characters of non-blank UTF-8 text, so
# refuse to write a line that would fail it instead of shipping it.
assert 1 <= len(LINE.strip()) <= 140, "fortune line must be 1-140 characters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
