import json
from pathlib import Path
import ajw

DATA_BASE_PATH = Path("/home/jvk/depromo/data_set.json")

if not DATA_BASE_PATH.exists():
    print("Database does not exist.")
    exit(0)

with open(DATA_BASE_PATH, "r") as f:
    data = json.load(f)

seen = set()
cleaned_data = {}

for key in sorted(data.keys(), key=int):
    msg = data[key]
    if msg not in seen:
        cleaned_data[key] = msg  # keep first occurrence
        seen.add(msg)

ajw.dump(cleaned_data, DATA_BASE_PATH)

print(f"Removed {len(data) - len(cleaned_data)} duplicate messages.")