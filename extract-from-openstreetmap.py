import sys
import urllib.parse
import requests
import datetime
import slugify # apt install python3-slugify
import os.path

def get_geo(nominatim_id):
    # geolocate
    geourl = f"https://nominatim.openstreetmap.org/lookup?osm_ids={nominatim_id}&format=jsonv2"
    rg = requests.get(geourl, headers={"User-Agent": "Stuart_nerdydaytrips/1.0"})
    g = rg.json()
    if g[0]["address"]["country_code"] != "gb":
        print("Sorry, this script doesn't handle non-UK stuff")
        sys.exit(2)
    return g

def get_osm(type, nodeid):
    # https://wiki.openstreetmap.org/wiki/API_v0.6 says to use
    # https://master.apis.dev.openstreetmap.org/ as api root, but
    # that doesn't work; the below URL is 404. So we use the main one.
    apiurl = f"https://api.openstreetmap.org/api/0.6/{type}/{nodeid}.json"
    j = requests.get(apiurl).json()
    return j

def syntax():
    print("Input URL should look like https://www.openstreetmap.org/node/950348332")
    print("Get it by right-clicking on the map on openstreetmap.org and say Query Features")
    print("Then pick a node from the Features list, or a way (not a 'relation')")
    print("If you pick a way (large buildings tend to be ways)")
    print("  try to pick a way which is a building, not a road,")
    print("  or the results will be weird and unexpected.")
    sys.exit(1)

osm_node_url = sys.argv[1]
parsed = urllib.parse.urlparse(osm_node_url)
parts = parsed.path.split("/")
if len(parts) != 3: syntax()
_, type, nodeid = parts
if type not in ["node", "way"]: syntax()
if not nodeid.isdigit(): syntax()

external_url = None
if type == "node":
    g = get_geo(f"N{nodeid}")
    j = get_osm("node", nodeid)
    lat = j["elements"][0]["lat"]
    lng = j["elements"][0]["lon"]
    if "url" in j["elements"][0]["tags"]:
        external_url = j["elements"][0]["tags"]["url"]
elif type == "way":
    g = get_geo(f"W{nodeid}")
    j = get_osm("way", nodeid)
    # ways list a bunch of nodes, and we don't want to fetch
    # them all because that hammers the API. Fortunately,
    # nominatim provides a bounding box, so we calculate the
    # centre point of that and use it as lat/lng for this way
    latmin, latmax, lngmin, lngmax = [float(x) for x in g[0]["boundingbox"]]
    lat = (latmin + latmax) / 2
    lng = (lngmin + lngmax) / 2
else:
    raise Exception("shouldn't happen")

region = "eu" # hardcode because we're gb only
address = g[0]["display_name"]
country = g[0]["address"]["country_code"]
title = j["elements"][0]["tags"]["name"]
title_slug = slugify.slugify(title)
slug = f"daytrip/{region}/{country}/{title_slug}"
output = {
    "slug": slug,
    "date": datetime.datetime.now().isoformat(timespec="seconds"),
    "lat": lat,
    "lng": lng,
    "location": address,
    "title": title
}
if external_url:
    output["external_url"] = external_url

filename = f"content/{slug}.md"
if os.path.exists(filename):
    print(f"Sorry, filename {filename} already exists; refusing to overwrite it")
    sys.exit(3)

lines = ["---\n"]
for k, v in output.items():
    lines.append(f"{k}: '{str(v).replace("'", "’")}'\n")
lines.append("---\n")
lines.append("\n")

if "--dry-run" in sys.argv:
    print(f"Not writing any file (although file written would have been {filename})")
else:
    with open(filename, mode="w") as fp:
        fp.writelines(lines)
    print(f"New item written as {filename}")
print("".join(lines))
