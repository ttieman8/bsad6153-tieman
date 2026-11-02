import json
import os
import time
import requests

BASE_URL = "https://api.opendota.com/api"

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/sample", exist_ok=True)

all_matches = []

for i in range(5):
    try:
        response = requests.get(
            f"{BASE_URL}/publicMatches",
            timeout=30
        )

        if response.status_code == 429:
            print("Rate limited. Waiting 30 seconds...")
            time.sleep(30)
            continue

        response.raise_for_status()

        matches = response.json()

        all_matches.extend(matches)

        print(f"Batch {i+1}: {len(matches)} matches")

        time.sleep(2)

    except requests.exceptions.Timeout:
        print("Timeout occurred")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

with open("data/raw/matches.json", "w") as f:
    json.dump(all_matches, f, indent=2)

with open("data/sample/sample_match.json", "w") as f:
    json.dump(all_matches[0], f, indent=2)

heroes = requests.get(
    f"{BASE_URL}/heroes",
    timeout=30
).json()

with open("data/raw/heroes.json", "w") as f:
    json.dump(heroes, f, indent=2)

print(f"Saved {len(all_matches)} matches")
print(f"Saved {len(heroes)} heroes")

