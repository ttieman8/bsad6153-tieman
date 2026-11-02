import json
import os
import requests

url = "https://api.opendota.com/api/publicMatches"

response = requests.get(url)

data = response.json()

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/sample", exist_ok=True)

with open("data/raw/matches.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data/sample/sample_match.json", "w") as f:
    json.dump(data[0], f, indent=2)

print(f"Saved {len(data)} matches")

