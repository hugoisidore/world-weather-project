from flask import Flask, Blueprint, render_template, redirect, url_for
import requests

forecast_app = Blueprint('forecast', __name__)

@forecast_app.route('/previsions')
def previsions():
    # Redirige vers une ville par défaut (ex: Paris)
    return redirect(url_for('forecast.forecast', city='Paris'))

@forecast_app.route('/forecast/<city>')
def forecast(city):
    # Requête API pour obtenir les prévisions sur 5 jours
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,  # Ville passée en paramètre
        "units": "metric",  # Unités Celsius
        "appid": "fb37b4abf3bf5b255e2741e5e5cc04da"
    }

    response = requests.get(url, params=params)
    forecast_data = {}

    # Vérification de la réponse
    if response.status_code == 200:
        forecast_data = response.json()
    else:
        print(f"Erreur {response.status_code}: {response.json().get('message')}")

    return render_template('forecast.html', city=city, forecast_data=forecast_data)
