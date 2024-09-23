import json

from weather.fetch.api_reservamos import fetch_destinations
from weather.fetch.api_open_weahter import fetch_weather

def fetch_forecast(q, page, per_page, show_all):
    destinations =fetch_destinations(q, page, per_page, show_all)
    print(destinations,"destinations")
    if destinations.status_code == 201:
        destinations = destinations.json()["data"]
        response = [fetch_weather_for_location(destination, "metric") for destination in destinations]
    elif destinations.status_code == 404:
        return []
    elif destinations.status_code != 201:
        return []
    else:
        return []

    return response

def fetch_weather_for_location(destination, units="metric"):
    weather = fetch_weather(destination["lat"], destination["long"], units)
    
    if weather.status_code == 200:
        weather = weather.json()
        print(len(weather),"longitud")
        destination["weather"] = weather
        return destination

    return {}
    

