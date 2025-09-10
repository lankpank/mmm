import requests, json, time

PLACE_ID = 85896571713843

def fetch_servers():
    servers = []
    cursor = ""
    while True:
        url = f"https://games.roblox.com/v1/games/{PLACE_ID}/servers/Public?sortOrder=Asc&limit=100"
        if cursor:
            url += f"&cursor={cursor}"
        r = requests.get(url).json()

        servers.extend(r.get("data", []))
        cursor = r.get("nextPageCursor")
        if not cursor:
            break
    return servers

if __name__ == "__main__":
    servers = fetch_servers()
    with open("servers.json", "w") as f:
        json.dump(servers, f, indent=2)
    print(f"Saved {len(servers)} servers at {time.ctime()}")
