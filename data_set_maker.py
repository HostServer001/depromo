import os
import ajw
import asyncio
import dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession
import json
from pathlib import Path

dotenv.load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")
MAX_DATA = 1000
GROUPS = ["Promotion_group2"]

client = TelegramClient(
    session=StringSession(STRING_SESSION),
    api_id=API_ID,
    api_hash=API_HASH
)

DATA_BASE_PATH = Path("/home/jvk/depromo/data_set.json")
if not DATA_BASE_PATH.exists():
    DATA_BASE_PATH.write_text("{}")

# Load database and set starting index
with open(DATA_BASE_PATH, "r") as f:
    data = json.load(f)

existing_messages = set(data.values())  # track all already stored messages

if data:
    n = max(map(int, data.keys())) + 1
else:
    n = 0

async def main():
    global n
    await client.start()

    for group in GROUPS:
        async for message in client.iter_messages(group, limit=None):
            # Skip messages already in the database
            if message.text in existing_messages:
                continue

            print(f"\nMessage ID {message.id} from {group}:")
            print(message.text)
            approve = input("Approve this message? (y/n): ").strip().lower()
            if approve == "y":
                ajw.append(n, message.text)
                existing_messages.add(message.text)  # update the set
                print(f"Message saved to database. [{n}/{MAX_DATA}] - {n/MAX_DATA*100:.2f}%")
                n += 1

            if n >= MAX_DATA:
                print("Reached MAX_DATA limit.")
                return

if __name__ == "__main__":
    asyncio.run(main())