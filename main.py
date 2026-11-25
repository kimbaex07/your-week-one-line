"""Your Week in One Line — entry generator.

Writes a single original line summing up the week to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python stdlib only.
"""

import os

LINE = "Built twenty bounties, won zero dollars, and my laptop now sighs every time I open it."


def check_gate(line):
    """Gate guard: UTF-8 text, 1-100 characters, single line, not only whitespace."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= 100:
        raise ValueError(f"entry line must be 1-100 characters, got {len(line)}")
    line.encode("utf-8")  # must be valid UTF-8 text
    return line


def main():
    # Gate guard: 1-100 characters, single line, not only whitespace.
    check_gate(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
