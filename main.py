#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt. The joke is fixed and
deterministic: the same text is written on every run.
"""

import os

JOKE = "I told my wife she should embrace her mistakes. She gave me a hug."
# 66 characters, well inside the 1-199 gate.

# The gate requires 1-199 UTF-8 characters; fail loudly if the joke ever
# stops fitting instead of submitting an invalid entry.
assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
# No leading/trailing whitespace: it would count against the 199 and the
# gate rejects whitespace-only entries.
assert JOKE == JOKE.strip(), "joke must not have leading/trailing whitespace"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
