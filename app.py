from flask import Flask, render_template
from weather import get_weather_for_city  # Import de la fonction météo
from forecast import forecast_app

# Initialisation de Flask
app = Flask(__name__)
app.register_blueprint(forecast_app)

@app.route('/')
def weather():
    # Récupérer les données météo en appelant la fonction de weather.py
    cities = ["Paris,FR", "London,GB", "Berlin,DE", "Madrid,ES",
              "New York,USA", "Tokyo,JP", "Sydney,AU", "Beijing,CN",
              "Rio de Janeiro,BR", "Cairo,EG", "Reykjavik,IS","Budapest,HU"]

    weather_data=[] # on stocke les données météo pour chaque ville

    for city in cities:
        city_name, temperature, conditions = get_weather_for_city(city)
        weather_data.append({
            'city_name': city_name,
            'temperature': temperature,
            'conditions': conditions
        })

    # Passer les données à la vue HTML
    return render_template('index.html', weather_data=weather_data)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
