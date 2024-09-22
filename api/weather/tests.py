from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch
# Create your tests here.

WEATHER_HEALTH = reverse("weather-api-health")
WEATHER_API = reverse("weather-api")

class WeatherTestCase(TestCase):
    def test_weather_endpoint_health(self):
        response = self.client.get(WEATHER_HEALTH)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    @patch("weather.views.requests.get")
    def test_weather_endpoint_health(self, mock_get):
        mock_response = [{
        "slug": "monterrey",
        "city_slug": "monterrey",
        "weekly_forecast": []
        }]
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.status_code = 200
        response = self.client.get(WEATHER_API)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), mock_response)