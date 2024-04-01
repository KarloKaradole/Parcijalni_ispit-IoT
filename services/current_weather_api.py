import openmeteo_requests
import requests_cache
from retry_requests import retry
    
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

def weather_temperature():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 43.7343,
        "longitude": 15.8942,
        "current": ["temperature_2m", "relative_humidity_2m", "pressure_msl"],
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]

    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()

    return(f"{round(current_temperature_2m,1)} \u00B0C")
   
def weather_humidity():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 43.7343,
        "longitude": 15.8942,
        "current": ["temperature_2m", "relative_humidity_2m", "pressure_msl"],
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]

    current = response.Current()
    current_relative_humidity_2m = current.Variables(1).Value()

    return(f"{round(current_relative_humidity_2m)} %")

def weather_pressure():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 43.7343,
        "longitude": 15.8942,
        "current": ["temperature_2m", "relative_humidity_2m", "pressure_msl"],
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]

    current = response.Current()
    current_pressure_msl = current.Variables(2).Value()

    return(f"{round(current_pressure_msl)} hPa")
