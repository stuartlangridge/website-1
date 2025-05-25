import sys
import urllib.parse
import requests
import datetime
import slugify # apt install python3-slugify
import os.path

def syntax():
    print("Input URL should look like https://www.openstreetmap.org/node/950348332")
    print("Get it by right-clicking on the map on openstreetmap.org and say Query Features")
    print("Then pick a node (not a way or a relation) from the Features list")
    sys.exit(1)

osm_node_url = sys.argv[1]
parsed = urllib.parse.urlparse(osm_node_url)
parts = parsed.path.split("/")
if len(parts) != 3: syntax()
_, type, nodeid = parts
if type not in ["node"]: syntax()
if not nodeid.isdigit(): syntax()

# geolocate
geourl = f"https://nominatim.openstreetmap.org/lookup?osm_ids=N{nodeid}&format=jsonv2"
rg = requests.get(geourl, headers={"User-Agent": "Stuart_nerdydaytrips/1.0"})
g = rg.json()
address = g[0]["display_name"]
if g[0]["address"]["country_code"] != "gb":
    print("Sorry, this script doesn't handle non-UK stuff")
    sys.exit(2)
country = g[0]["address"]["country_code"]
region = "eu" # hardcode because we're gb only

# https://wiki.openstreetmap.org/wiki/API_v0.6 says to use
# https://master.apis.dev.openstreetmap.org/ as api root, but
# that doesn't work; the below URL is 404. So we use the main one.
apiurl = f"https://api.openstreetmap.org/api/0.6/node/{nodeid}.json"

j = requests.get(apiurl).json()
title = j["elements"][0]["tags"]["name"]
title_slug = slugify.slugify(title)
slug = f"daytrip/{region}/{country}/{title_slug}"
output = {
    "slug": slug,
    "date": datetime.datetime.now().isoformat(timespec="seconds"),
    "lat": j["elements"][0]["lat"],
    "lng": j["elements"][0]["lon"],
    "location": address,
    "title": title
}
if "url" in j["elements"][0]["tags"]:
    output["externalurl"] = j["elements"][0]["tags"]["url"]
filename = f"content/{slug}.md"
if os.path.exists(filename):
    print(f"Sorry, filename {filename} already exists; refusing to overwrite it")
    sys.exit(3)

lines = ["---\n"]
for k, v in output.items():
    lines.append(f"{k}: {v}\n")
lines.append("---\n")
lines.append("\n")

with open(filename, mode="w") as fp:
    fp.writelines(lines)
print(f"New item written as {filename}")
print("".join(lines))