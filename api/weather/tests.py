from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch
from rest_framework.response import Response


from weather.fetch.api_reservamos import fetch_destinations
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
        mock_get.return_value = Response(mocked_data, status=status.HTTP_200_OK)

        response = self.client.get(WEATHER_API)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), mocked_data)


    @patch("weather.fetch.api_reservamos.fetch_destinations")
    def test_reservamos_destinations_api_fetch(self, mock_fetch):
        mock_fetch.return_value = [{
            "slug": "monterrey",
            "city_slug": "monterrey",
        }]
        response = fetch_destinations()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), mock_fetch.return_value)
        