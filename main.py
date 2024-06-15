import requests
import os

API_KEY = os.getenv("API_KEY")

locations = [
    "Ancol",
    "Cilincing",
    "Kalibaru",
    "Kamal Muara",
    "Kapuk Muara",
    "Kebon Bawang",
    "Kelapa Gading Barat",
    "Kelapa Gading Timur",
    "Koja",
    "Lagoa",
    "Marunda",
    "Pademangan Barat",
    "Pademangan Timur",
    "Papanggo",
    "Pegangsaan Dua",
    "Pejagalan",
    "Penjaringan",
    "Pluit",
    "Rawa Badak Selatan",
    "Rawa Badak Utara",
    "Rorotan",
    "Semper Barat",
    "Semper Timur",
    "Sukapura",
    "Sungai Bambu",
    "Sunter Agung",
    "Sunter Jaya",
    "Tanjung Priok",
    "Tugu Selatan",
    "Tugu Utara",
    "Warakas",
    # Add more locations from KEMAYORAN and HALIM
]


def get_lat_lng(location):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json().get("results")
        if result:
            location_data = result[0].get("geometry").get("location")
            return location_data.get("lat"), location_data.get("lng")
    return None, None


location_coordinates = {}

for location in locations:
    lat, lng = get_lat_lng(location)
    if lat is not None and lng is not None:
        location_coordinates[location] = (lat, lng)
    else:
        location_coordinates[location] = "Coordinates not found"

for location, coordinates in location_coordinates.items():
    print(f"{location}: {coordinates}")
