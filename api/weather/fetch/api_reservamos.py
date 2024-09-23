import requests
import os
import json

from requests import Response as RequestsResponse
from requests.models import Response

from utils.pagination import get_total_pages, paginate_list

# Adding json example for preventing over-fetching api (MIGHT BE DELETED AFTER DEVELOPMENT)
with open("examples/reservamos-api-response.json") as f:
    data = json.load(f)

def get_fake_response():
    response = RequestsResponse()
    response.status_code = 201
    response._content = json.dumps(data).encode()
    return response

def fetch_destinations(q, page, per_page, show_all):
    return get_fake_response()
    api_uri = os.environ.get("RESERVAMOS_API_URI")
    url = f"{api_uri}?q={q}"
    response = requests.get(url)
    if response.status_code == 404:
        return response
    if response.status_code != 201:
        return response
    data = response.json()
    total_items = len(data)
    if show_all:
        return response
    total_pages = get_total_pages(total_items, per_page)
    if page > total_pages:
        response.status_code = 400
        return response
    paginated_data = paginate_list(data, page, per_page)
    response._content = json.dumps(paginated_data).encode()
    return response