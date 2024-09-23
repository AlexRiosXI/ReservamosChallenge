import requests
import os
import json

from collections import defaultdict

from requests import Response as RequestsResponse


# Criteria for filtering weather data by hour
hour_filter = [int(x) for x in os.getenv("WEATHER_HOUR_FILTER").split(",")] if os.getenv("WEATHER_HOUR_FILTER") else [15]

# Adding json example for preventing over-fetching api (MIGHT BE DELETED AFTER DEVELOPMENT)
with open("examples/open-weather-api-response.json") as f:
    data = json.load(f)

def get_fake_response():
    response = RequestsResponse()
    response.status_code = 200
    response._content = json.dumps(data).encode()
    weather = clean_weather_data(response.json())
    response._content = json.dumps(weather).encode()
    
    return response


def fetch_weather(lat,long,units="metric"):
    return get_fake_response()
    api_uri = os.environ.get("OPEN_WEATHER_API_URI")
    url = f"{api_uri}?q='mont'"
    response = requests.get(url)
    return response


def clean_weather_data(data):
    filtered_date_times = []
    for item in data['list']:
        dt_txt = item['dt_txt']
        hour = int(dt_txt.split()[1].split(':')[0])
        # Check if the hour is in the hour filter
        if hour in hour_filter:
            item = {
                'date': dt_txt,
                "date_time": item["dt"],
                "temp": item["main"]["temp"],
                "feels_like": item["main"]["feels_like"],
                "humidity": item["main"]["humidity"],
                "temp_max": item["main"]["temp_max"],
                "temp_min": item["main"]["temp_min"],
                "pressure": item["main"]["pressure"],
                "wind" : {
                    "speed": item["wind"]["speed"],
                    "deg": item["wind"]["deg"]
                },
                "clouds": item["clouds"],
                "weather_description": item["weather"][0]["description"] if len(item["weather"]) > 0 else "",       
                "weather_icon": item["weather"][0]["icon"] if len(item["weather"]) > 0 else "",
            }
            filtered_date_times.append(item)

    return filtered_date_times


    
