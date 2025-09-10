import requests
import json

# Your game placeId
place_id = "85896571713843"

# Your Discord webhook
webhook_url = "https://discord.com/api/webhooks/1411629941178765365/k0Tw3CWiuZ935oPnQ4GnofN3xcWAc7q3KWg41_SwqtkOlyNotA5nNXzPjf1XVg1zcu4h"

# Roblox servers API
url = f"https://games.roblox.com/v1/games/{place_id}/servers/Public?sortOrder=Asc&limit=100"

all_servers = []
cursor = None

while True:
    query_url = url if not cursor else url + f"&cursor={cursor}"
    response = requests.get(query_url)
    data = response.json()

    if "data" not in data or len(data["data"]) == 0:
        break

    all_servers.extend(data["data"])
    cursor = data.get("nextPageCursor")
    if not cursor:
        break

# Save to file
with open("servers.json", "w") as f:
    json.dump(all_servers, f, indent=2)

# Send Discord message
message = {"content": f"✅ Fetched {len(all_servers)} servers from Roblox"}
requests.post(webhook_url, json=message)

print(f"✅ Done! {len(all_servers)} servers fetched and saved.")
