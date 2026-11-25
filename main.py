"""Dictionary Deletion — the one-word entry for make.fun.

The bounty asks for a single word to erase from the dictionary
forever, with nothing else attached. This program loads that word
from output/entry.txt and prints it — the word is the whole entry.

My pick: "colonel". It is spelled nothing like it sounds ("kernel"),
so deleting it removes one of English's great spelling crimes.
"""

from pathlib import Path


def load_condemned_word(entry_path):
    """Read the condemned word, stripped of surrounding whitespace."""
    return Path(entry_path).read_text(encoding="utf-8").strip()


def require_single_word(word):
    """The bounty takes one word and nothing else attached."""
    if not word or len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return word


def main():
    entry_path = Path(__file__).resolve().parent / "output" / "entry.txt"
    word = require_single_word(load_condemned_word(entry_path))
    print(word)


if __name__ == "__main__":
    main()
