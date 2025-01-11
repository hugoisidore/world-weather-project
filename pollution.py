from pyowm import OWM

# Clé API
api_key = "fb37b4abf3bf5b255e2741e5e5cc04da"
owm = OWM(api_key)
air_quality_manager = owm.airpollution_manager()

def get_city_coordinates(city_name):
    """
    on  récupère les coordonnées géographiques d'une ville à partir de son nom.
    """
    geocoder = owm.geocoding_manager()
    locations = geocoder.geocode(city_name, limit=1)
    if locations:
        location = locations[0]
        return location.lat, location.lon
    else:
        raise ValueError(f"Ville '{city_name}' introuvable.")

def get_air_pollution(lat, lon):
    """
    on récupère les données de pollution de l'air pour des coordonnées données.
    """
    air_quality = air_quality_manager.air_quality_at_coords(lat, lon)
    return {
        "PM10": air_quality.pm10,
        "AQI": air_quality.aqi,
        "CO": air_quality.co,
        "NO": air_quality.no,
        "NO2": air_quality.no2,
        "O3": air_quality.o3,
        "SO2": air_quality.so2,
        "NH3": air_quality.nh3,
    }
