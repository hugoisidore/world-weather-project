import requests
from flask import Flask, request, jsonify, render_template
from pyowm import OWM

app = Flask(__name__)

owm = OWM('fb37b4abf3bf5b255e2741e5e5cc04da')
mgr = owm.weather_manager()


@app.route('/')
def index():
    # Obtenir l'adresse IP de l'utilisateur
    user_ip = request.remote_addr if request.remote_addr != '127.0.0.1' else '8.8.8.8'

    # Utiliser l'API de géolocalisation pour obtenir la position
    geo_api_url = f'http://ip-api.com/json/{user_ip}'
    geo_response = requests.get(geo_api_url).json()

    # Extraire les coordonnées et la ville
    if geo_response['status'] == 'success':
        latitude = geo_response['lat']
        longitude = geo_response['lon']
        city = geo_response['city']
    else:
        latitude, longitude, city = None, None, None

    # Si la géolocalisation a fonctionné, obtenir la météo
    if latitude and longitude:
        observation = mgr.weather_at_coords(latitude, longitude)
        weather = observation.weather
        temperature = weather.temperature('celsius')['temp']
        description = weather.detailed_status

        return render_template('index.html', city=city, temperature=temperature, description=description)

    # En cas d'échec, afficher un formulaire
    return render_template('index.html', error="Impossible d'obtenir votre position.")
