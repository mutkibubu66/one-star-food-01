import os

MAX_CHARS = 200

PART1 = "One star: the gravity here broke my "
PART2 = "luggage and the oceans are "
PART3A = "undrinkable, yet the biryani "
PART3B = "alone was "
PART4 = "worth the forty-light-year trip."
LINE = PART1 + PART2 + PART3A + PART3B + PART4

assert 1 <= len(LINE) <= MAX_CHARS, "entry must be 1-200 characters"
assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be exactly one sentence"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE, "round-trip mismatch"
print(len(LINE))
