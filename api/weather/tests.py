from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch, MagicMock
from rest_framework.response import Response
from requests import Response as RequestsResponse

import json


from weather.fetch.api_reservamos import fetch_destinations
from weather.fetch.api_open_weahter import fetch_weather

from utils.pagination import get_total_pages, paginate_list
# Create your tests here.

WEATHER_HEALTH = reverse("weather-api-health")
WEATHER_API = reverse("weather-api")


class WeatherTestCase(TestCase):
    def test_weather_endpoint_health(self):
        response = self.client.get(WEATHER_HEALTH)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch("weather.views.WeatherAPIView.get")
    def test_weather_api(self, mock_get):

        mocked_data = [{
            "slug": "monterrey",
            "city_slug": "monterrey",
            "weekly_forecast": []
        }]
        mock_get.return_value = Response(mocked_data, status=201)

        response = self.client.get(WEATHER_API)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), mocked_data)


    @patch("weather.fetch.api_reservamos.requests.get")
    def test_reservamos_destinations_api_fetch(self, mock_get):
        mocked_data = [{
            "slug": "monterrey",
            "city_slug": "monterrey",
        }]
        mock_response = MagicMock()
        mock_response.status_code = status.HTTP_201_CREATED
        mock_response.json.return_value = mocked_data
        mock_get.return_value = mock_response
        q = "mont"
        page = 1
        per_page = 10
        show_all = False

        response = fetch_destinations(q, page, per_page, show_all)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), mocked_data)
        
    """
    @patch("weather.fetch.api_open_weahter.requests.get")
    def test_open_weather_destinations_api_fetch(self, mock_get):
        mocked_data = [{
            "slug": "monterrey",
            "city_slug": "monterrey",
        }]
        mock_response = MagicMock()
        mock_response.status_code = status.HTTP_201_CREATED
        mock_response.json.return_value = mocked_data
        mock_get.return_value = mock_response

        response = fetch_weather()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), mocked_data)"""
    

class PaginationTestCase(TestCase):
    def test_get_total_pages(self):
        total_items = 101
        per_page = 10
        total_pages = get_total_pages(total_items, per_page)
        self.assertEqual(total_pages, 11)
        total_items = 56
        per_page = 20
        total_pages = get_total_pages(total_items, per_page)
        self.assertEqual(total_pages, 3)
        total_items = 71
        per_page = 35
        total_pages = get_total_pages(total_items, per_page)
        self.assertEqual(total_pages, 3)

    def test_get_total_pages_fail(self):
        total_items = 101        
        per_page = 10
        total_pages = get_total_pages(total_items, per_page)
        self.assertNotEqual(total_pages, 10)
        total_items = 71
        per_page = 35
        total_pages = get_total_pages(total_items, per_page)
        self.assertNotEqual(total_pages, 2)

    def test_paginate_list(self):
        items = [i for i in range(1, 17)]
        page = 1
        per_page = 10
        paginated_items = paginate_list(items, page, per_page)
        self.assertEqual(paginated_items, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        page = 2
        per_page = 10
        paginated_items = paginate_list(items, page, per_page)        
        self.assertEqual(paginated_items, [11, 12, 13, 14, 15, 16])
        page = 3
        per_page = 5
        paginated_items = paginate_list(items, page, per_page)
        self.assertEqual(paginated_items, [11, 12, 13, 14, 15])
