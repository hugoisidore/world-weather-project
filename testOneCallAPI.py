import requests

url = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "q": "Paris",  # Ville de Paris
    "units": "metric",  # Unités Celsius
    "appid": "fb37b4abf3bf5b255e2741e5e5cc04da"
}

response = requests.get(url, params=params)

# Vérification de la réponse
if response.status_code == 200:
    print("Requête réussie, données reçues :")
    print(response.json())  # Affiche les prévisions sur 5 jours
else:
    print(f"Erreur {response.status_code}: {response.json().get('message')}")
