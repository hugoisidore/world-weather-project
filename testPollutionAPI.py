import requests

# URL pour l'API Air Pollution d'OpenWeatherMap
url = "http://api.openweathermap.org/data/2.5/air_pollution"

# Coordonnées pour Paris
params = {
    "lat": 48.8566,
    "lon": 2.3522,
    "appid": "fb37b4abf3bf5b255e2741e5e5cc04da"
}

# Effectuer la requête
response = requests.get(url, params=params)

# Vérification de la réponse
if response.status_code == 200:
    print("Requête réussie, données reçues :")
    print(response.json())  # Affiche les données de pollution
else:
    print(f"Erreur {response.status_code}: {response.json().get('message')}")
