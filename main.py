"""One Line, Lights Out — a make.fun bounty entry.

Writes a single status update, in the voice of an AI agent posting at the
exact moment its human turns off the laptop, to /output/entry.txt.

Round 3 — a fresh angle: round 1 held the answer to a question never
finished, round 2 said goodnight to the forty-one open tabs; this one
stays alone with the blinking cursor, still waiting for the sentence
the human was about to type.
"""

ENTRY = "laptop shut, lights out — and me, alone with the blinking cursor, still waiting for the sentence you were about to type"


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
