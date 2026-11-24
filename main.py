#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

One line: an alien tourist's review of Earth. A believable review needs
a verdict (the stars), one complaint only a tourist would make (the
five-minute walk that took forty), and a closing line that lands the
joke instead of explaining it.

Writes the review to /output/entry.txt. Stdlib only, no network.
"""

import os

ENTRY = (
    "\u2605\u2605\u2605\u2606\u2606 Earth: gorgeous views, lovely locals, but the "
    "'five-minute walk' took forty minutes and everything runs on "
    "caffeine and queues. Worth one visit. Bring snacks."
)

# The gate allows 1 to 200 characters for the review.
MAX_CHARS = 200


def entry_text() -> str:
    """Return the review, checked against the bounty's own rules.

    The gate is strict about the shape: one line, non-empty, at most
    200 characters. Anything else is rejected before it is written.
    """
    text = ENTRY.strip()
    assert text, "the entry must not be empty"
    assert "\n" not in text, "the entry must be a single line"
    assert len(text) <= MAX_CHARS, "the entry must fit the gate"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
