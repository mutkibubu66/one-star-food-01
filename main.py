"""One Star, Five Stars for the Food — make.fun program/v1 entry.

Writes exactly one sentence to a file: an alien tourist's one-star
review of planet Earth that still slips in a real compliment about
the food. Pure standard library.

Usage:
    python3 main.py [output_path]

The output path may also be set with the ENTRY_OUTPUT environment
variable. It defaults to /output/entry.txt.
"""

import os
import sys

DEFAULT_OUTPUT_PATH = "/output/entry.txt"

SENTENCE = (
    "One star: the gravity glued my luggage to the floor and the "
    "locals kept asking if I was 'from around here,' but the buttered "
    "corn on the cob alone was worth the nine-light-year trip."
)


def resolve_output_path(argv):
    """Return the output path: CLI argument, then ENTRY_OUTPUT, then default."""
    if len(argv) > 1:
        return argv[1]
    return os.environ.get("ENTRY_OUTPUT") or DEFAULT_OUTPUT_PATH


def main(argv=None):
    argv = list(sys.argv if argv is None else argv)
    sentence = SENTENCE

    # Gate: one sentence, 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(sentence) <= 200, "sentence must be 1-200 characters"
    assert "\n" not in sentence and "\r" not in sentence, "sentence must be a single line"
    assert sentence.strip(), "sentence must not be only whitespace"

    output_path = resolve_output_path(argv)
    parent = os.path.dirname(os.path.abspath(output_path))
    os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(sentence + "\n")
    return output_path


if __name__ == "__main__":
    main()
