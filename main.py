#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt. The joke is fixed and
deterministic: the same text is written on every run.
"""

import os

JOKE = "I told my wife she should embrace her mistakes. She gave me a hug."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
