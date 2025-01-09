import io
import base64
import requests
import matplotlib
matplotlib.use('Agg')  # On désactive l'interface graphique de Matplotlib pour éviter le problème avec macOS
import matplotlib.pyplot as plt
from flask import Flask, Blueprint, render_template, redirect, url_for
from matplotlib.ticker import MaxNLocator

forecast_app = Blueprint('forecast', __name__)


@forecast_app.route('/previsions')
def previsions():
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

    # Générer le graphique
    img = generate_graph(forecast_data)

    # Convertir l'image en base64 pour l'envoyer dans le HTML
    img_str = base64.b64encode(img).decode('utf-8')

    return render_template('forecast.html', city=city, forecast_data=forecast_data, img_data=img_str)


def generate_graph(forecast_data):
    # Créer un graphique avec Matplotlib
    dates = []
    temperatures = []

    for day in forecast_data['list']:
        dates.append(day['dt_txt'])
        temperatures.append(day['main']['temp'])

    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, label='Température (°C)', color='tab:blue')

    ax.set_xlabel('Date')
    ax.set_ylabel('Température (°C)')
    ax.set_title('Prévisions Météo sur 5 jours')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=6))
    ax.tick_params(axis='x', rotation=45)

    # Convertir l'image en format PNG pour l'envoyer comme réponse HTTP
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)

    return img.read()
