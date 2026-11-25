"""Describe Your Ex in One Word (make.fun).

Writes a single-word verdict on an ex to /output/entry.txt.
Pure standard library; deterministic: the same word every run.

Entry: "Understudy" -- the ex never got the lead role; he spent the
whole relationship waiting in the wings as the backup. One word,
spelled correctly, no punctuation tricks, instantly readable as a
verdict on a former partner.
"""

import os

ENTRY = "Understudy"

# Gate (mirrors the bounty scorer): entry.txt must be UTF-8 text of
# 1 to 111 characters, not only whitespace, exactly one word, spelled
# correctly, no punctuation tricks.
assert 1 <= len(ENTRY) <= 111, "entry must be 1-111 characters"
assert ENTRY.strip() == ENTRY, "entry must have no surrounding whitespace"
assert len(ENTRY.split()) == 1, "entry must be exactly one word"
assert ENTRY.isalpha(), "entry must be a single alphabetic word"


def main() -> None:
    path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(ENTRY)
    except OSError:
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w",
                  encoding="utf-8") as handle:
            handle.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
