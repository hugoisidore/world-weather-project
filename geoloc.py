import requests
from flask import Flask, request, render_template
from pyowm import OWM

app = Flask(__name__)

owm = OWM('fb37b4abf3bf5b255e2741e5e5cc04da')
mgr = owm.weather_manager()


@app.route('/')
def index():
    # Obtenir l'adresse IP de l'utilisateur
    user_ip = request.remote_addr if request.remote_addr != '127.0.0.1' else '8.8.8.8'

    # Utiliser l'API ip-api pour obtenir la position géographique
    geo_api_url = f'http://ip-api.com/json/{user_ip}'
    geo_response = requests.get(geo_api_url).json()

    city = None
    temperature = None
    conditions = None

    # Si géolocalisation réussie, récupérer les données météo
    if geo_response.get('status') == 'success':
        city = geo_response['city']
        latitude = geo_response['lat']
        longitude = geo_response['lon']

        # Obtenir les informations météo pour les coordonnées
        observation = mgr.weather_at_coords(latitude, longitude)
        weather = observation.weather
        temperature = weather.temperature('celsius')['temp']
        conditions = weather.detailed_status

    # Transmettre les données géolocalisées au template
    return render_template(
        'index.html',
        localized_weather={
            'city': city or '',
            'temperature': temperature or '',
            'conditions': conditions or ''
        }
    )
