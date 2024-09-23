
from weather.fetch.api_reservamos import fetch_destinations
def fetch_forecast(q, page, per_page, show_all):
    destinations =fetch_destinations(q, page, per_page, show_all)
    return destinations