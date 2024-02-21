import sys
import requests
from managek2App.models import StateDistrict

# Add the directory containing your Django project to the Python path
sys.path.append('/home/ubuntu/krishikutumbv1')

# Replace 'YOUR_MAPBOX_API_KEY' with your actual Mapbox API key
MAPBOX_API_KEY = 'pk.eyJ1IjoiYXNtaXRhMzAiLCJhIjoiY2xrd2NzZWluMDlrNjNkbjBpajh4dHc4byJ9.gELlWug5XvGdMhodqOfUkw'

# Read a limited number of rows from your existing village data in the database
query = StateDistrict.objects.using('secondary').all()[:100]
# Now 'query' contains the result of your SQL query

# Function to perform geocoding using Mapbox API
def geocode_mapbox(state, district):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{state},{district}.json"
    params = {
        "access_token": MAPBOX_API_KEY,
        "limit": 1  # We only want the top result
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data.get("features"):
        coordinates = data["features"][0]["geometry"]["coordinates"]
        return coordinates[1], coordinates[0]  # Mapbox returns longitude first, then latitude
    else:
        return None, None

# Iterate over rows and generate lat, long, and geom values
for row in query:
    lat, lon = geocode_mapbox(row.state, row.district)
    if lat is not None and lon is not None:
        row.latitude = lat
        row.longitude = lon
        row.geom = f"POINT({lon} {lat})"
        row.save()

print("Data successfully updated in the existing table.")
