import openmeteo_requests
import requests_cache
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

def daily_temperature():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 43.7343,
        "longitude": 15.8942,
        "hourly": ["temperature_2m"],
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]

    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_temperature_2m_rounded = [round(float(value), 1) for value in hourly_temperature_2m]
    
    return hourly_temperature_2m_rounded

def daily_humidity():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 43.7343,
        "longitude": 15.8942,
        "hourly": ["relative_humidity_2m"],
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]

    hourly = response.Hourly()
    hourly_relative_humidity_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_relative_humidity_2m_rounded = [round(value) for value in hourly_relative_humidity_2m]
    
    return hourly_relative_humidity_2m_rounded

def daily_pressure():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 43.7343,
        "longitude": 15.8942,
        "hourly": ["pressure_msl"],
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]

    hourly = response.Hourly()
    hourly_pressure_msl = hourly.Variables(0).ValuesAsNumpy()

    hourly_pressure_msl_rounded = [round(value) for value in hourly_pressure_msl]
    
    return hourly_pressure_msl_rounded

