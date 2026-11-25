"""makefun-invent-word-01: a newly coined English word, one line."""

import os

ENTRY = "Tablapse \u2014 the instant blank when a new tab opens, wiping out why you opened it."

if __name__ == "__main__":
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
