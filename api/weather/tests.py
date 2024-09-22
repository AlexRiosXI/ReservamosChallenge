from django.test import TestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here.

WEATHER_HEALTH = reverse("weather-api-health")

class WeatherTestCase(TestCase):
    def test_weather_endpoint_health(self):
        response = self.client.get(WEATHER_HEALTH)
        self.assertEqual(response.status_code, status.HTTP_200_OK)