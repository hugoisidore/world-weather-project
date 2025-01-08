from flask import Flask, render_template
from weather import get_weather  # Import de la fonction météo

# Initialisation de Flask
app = Flask(__name__)

@app.route('/')
def weather():
    # Récupérer les données météo en appelant la fonction de weather.py
    temperature, conditions = get_weather()

    # Passer les données à la vue HTML
    return render_template('index.html', temperature=temperature, conditions=conditions)

if __name__ == '__main__':
    app.run(debug=True)
