import json
from pathlib import Path
from collections import Counter

DATA_BASE_PATH = Path("/home/jvk/depromo/data_set.json")

if not DATA_BASE_PATH.exists():
    print(0)
    exit(0)


with open(DATA_BASE_PATH, "r") as f:
    data = json.load(f)

messages = list(data.values())


counter = Counter(messages)

useless_count = sum(count - 1 for count in counter.values() if count > 1)

print(useless_count)