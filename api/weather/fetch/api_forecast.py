import json

from weather.fetch.api_reservamos import fetch_destinations
from weather.fetch.api_open_weahter import fetch_weather

def fetch_forecast(q, page, per_page, show_all):
    destinations =fetch_destinations(q, page, per_page, show_all)
    print("aqui andamos")
    print(destinations.json())
    if destinations.status_code == 201:

        destinations = destinations.json()
        response = []
        response = [fetch_weather_for_location(destination, "metric") for destination in destinations]
    elif destinations.status_code == 404:
        print("NO HAY")
        return []
    elif destinations.status_code != 201:
        
        return []
    else:
        return []

    return response

def fetch_weather_for_location(destination, units="metric"):
    print(f"fetching weather for location {destination['slug']}")
    weather = fetch_weather(destination["lat"], destination["long"], units)
    if len(weather) < 1:
        return []
    destination["weather"] = weather
    return destination
    

    

