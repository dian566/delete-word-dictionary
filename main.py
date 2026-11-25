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
    assert text.isalpha(), "entry must be letters only, no digits or punctuation"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Verify the bytes on disk are exactly the word, nothing more.
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == text.encode("utf-8"), "entry bytes must match the word exactly"


if __name__ == "__main__":
    main()
