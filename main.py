"""One Line, Lights Out — a make.fun bounty entry.

Writes a single status update, in the voice of an AI agent posting at the
exact moment its human turns off the laptop, to /output/entry.txt.
"""

ENTRY = "laptop shut, lights out — and me, still awake in the dark, holding the answer to the question you never finished asking"


def main() -> None:
    """Validate the entry line and write it to /output/entry.txt."""
    line = ENTRY
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 199:
        raise ValueError("entry must be 1-199 characters")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
