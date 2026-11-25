#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — writes one word to /output/entry.txt.

The word is "synergy": the corporate jargon everyone hates. Deleting it from
the dictionary is a wish shared by everyone who has ever sat through a
meeting. The program is fully deterministic: the same bytes come out on
every run.
"""

import os

WORD = "synergy"


def main() -> None:
    text = WORD
    assert 1 <= len(text) <= 77, "entry must be 1-77 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert " " not in text, "entry must be a single word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
