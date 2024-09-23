import requests
import os
import json

from collections import defaultdict

from requests import Response as RequestsResponse
import httpx 

from dotenv import load_dotenv
load_dotenv()


# Criteria for filtering weather data by hour
hour_filter = [int(x) for x in os.getenv("WEATHER_HOUR_FILTER").split(",")] if os.getenv("WEATHER_HOUR_FILTER") else [15]

def fetch_weather(lat,long,units="metric"):
    api_uri = os.environ.get("OPENWEATHER_AP2I_URI")
    headers = { 'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"} # This is chrome, you can set whatever browser you like
    url = f"{api_uri}?lat={lat}&lon={long}&units={units}&appid={os.getenv('OPEN_WEATHER_API_KEY')}"
    response = httpx.get(url, headers=headers)
    print("fetched")
    if response.status_code == 200:
        response = clean_weather_data(response.json())
    elif response.status_code == 404:
        response = []
    else:
        response = []
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


    
