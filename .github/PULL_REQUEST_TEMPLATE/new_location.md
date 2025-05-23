---
name: New Location
about: Add a new location to the map
title: "Add location: [Location Name]"
labels: new-location
assignees: ''

---

**Location Name**
[Name of the location]

**Latitude and Longitude**
Please provide the GPS coordinates for this location.
You can use a tool like [Google Maps](https://www.google.com/maps) or [OpenStreetMap](https://www.openstreetmap.org) to find these.
- Latitude: [e.g. 41.0683790]
- Longitude: [e.g. -81.5459300]

**Description**
Please provide a description of the location. Markdown is supported.

**Front Matter Template**
Here is a template for the front matter. Please replace the placeholder values with the correct information.

```yaml
---
slug: "daytrip/na/us/your-location-name"  # Replace with the correct slug (continent/country/city-or-region/location-name)
date: 'YYYY-MM-DDTHH:MM:SS' 
lat: 'YOUR_LATITUDE'
lng: 'YOUR_LONGITUDE'
location: "Optional: A human-readable location string"
title: "Your Location Name"
---
```

**Checklist**
- [ ] I have added the correct latitude and longitude.
- [ ] I have added a descriptive title.
- [ ] I have added a description of the location.
- [ ] I have filled in the front matter template.
