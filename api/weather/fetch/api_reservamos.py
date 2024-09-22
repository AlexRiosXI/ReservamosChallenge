import requests
import os
def fetch_destinations():
    api_uri = os.environ.get("RESERVAMOS_API_URI")
    url = f"{api_uri}?q='mont'"
    response = requests.get(url)
    return response