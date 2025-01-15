import requests
from flask import Blueprint, request, render_template
from pyowm import OWM

geoloc_blueprint = Blueprint('geoloc', __name__)

owm = OWM('fb37b4abf3bf5b255e2741e5e5cc04da')
mgr = owm.weather_manager()


@geoloc_blueprint.route('/debug')
def debug_geoloc():
    # Obtenir l'adresse IP de l'utilisateur
    user_ip = request.remote_addr if request.remote_addr != '127.0.0.1' else '1.1.1.1'

    # Utiliser l'API ip-api pour obtenir la position géographique
    geo_api_url = f'http://ip-api.com/json/{user_ip}'
    geo_response = requests.get(geo_api_url).json()
    print(f"Géo-response brute: {geo_response}")  # pour visualiser la rép dans la console

    city = None
    temperature = None
    conditions = None

    # Si géolocalisation réussie, récupérer les données météo
    if geo_response.get('status') == 'success':
        print("Géolocalisation réussie.")
        city = geo_response['city']
        latitude = geo_response['lat']
        longitude = geo_response['lon']
        print(f"Ville : {city}, Latitude : {latitude}, Longitude : {longitude}")

        # Obtenir les informations météo pour les coordonnées
        observation = mgr.weather_at_coords(latitude, longitude)
        print("Observation météo obtenue.")
        weather = observation.weather
        temperature = weather.temperature('celsius')['temp']
        conditions = weather.detailed_status
        print(f"Température : {temperature}, Conditions : {conditions}")
    else:
        print("Erreur de géolocalisation ou réponse invalide.")

# Transmettre les données géolocalisées au template
    return render_template(
        'index.html',
        localized_weather={
            'city': city or '',
            'temperature': temperature or '',
            'conditions': conditions or ''
        }
    )
print("Le fichier geoloc.py a bien été exécuté.")
