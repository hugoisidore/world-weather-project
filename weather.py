from pyowm.owm import OWM
from colorama import Fore
from tabulate import tabulate

# Clé API
api_key = "fb37b4abf3bf5b255e2741e5e5cc04da"

def get_weather():
    owm = OWM(api_key)
    mgr = owm.weather_manager()

    # Récupérer les conditions météo pour Paris
    weather = mgr.weather_at_place("Paris,FR").weather
    temperature = weather.temperature('celsius')['temp']
    conditions = weather.detailed_status

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

    return temperature, conditions