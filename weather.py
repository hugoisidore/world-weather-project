from pyowm.owm import OWM
from colorama import Fore
from tabulate import tabulate

# Clé API
api_key = "fb37b4abf3bf5b255e2741e5e5cc04da"

def get_weather_for_city(city_name):
    owm = OWM(api_key)
    mgr = owm.weather_manager()

    # Récupérer les conditions météo
    weather = mgr.weather_at_place(city_name).weather
    temperature = weather.temperature('celsius')['temp']
    conditions = weather.detailed_status

    return city_name, temperature, conditions

def display_weather_for_multiple_cities(cities):
    for city in cities:
        city_name, temperature, conditions = get_weather_for_city(city)

    # Créer le tableau avec des couleurs
    data = [
        [Fore.CYAN + "Température", Fore.YELLOW + f"{temperature:.2f}°C"],
        [Fore.CYAN + "Conditions", Fore.YELLOW + conditions.capitalize()]
    ]

    # Affichage avec colorama
    print(Fore.GREEN + "=" * 40)  # Ligne de séparation
    print(Fore.RED + "Météo actuelle pour Paris".center(40))
    print(Fore.GREEN + "=" * 40)
    print(tabulate(data, headers=[Fore.CYAN + "Détail", Fore.YELLOW + "Valeur"], tablefmt="grid"))
    print(Fore.GREEN + "=" * 40)

    cities = ["Paris,FR","New York,USA","Tokyo,JP", "London,GB", "Berlin,DE",
          "Sydney,AU", "Beijing,CN", "Rio de Janeiro,BR", "Cairo,EG", "Madrid,ES"]


    display_weather_for_multiple_cities(cities)

