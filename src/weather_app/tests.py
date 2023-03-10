
from weather_app.models import Weather, Stats
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class WeatherTestCase(APITestCase):
    """
        Test Weather Endpoints
    """

    def test_get_weather(self):
        Weather.objects.create(
            station_name="USC001107", date="1985010", max_temp=20, min_temp=19, precipitation=12)
        response = self.client.get(reverse("weather-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)
        self.assertEqual(response.data["count"], 1)


class StatsTestCase(APITestCase):
    """
        Test Stats Endpoints
    """

    def test_get_stats(self):
        Stats.objects.create(
            date='2022-01-01',
            station_name='Test Station',
            avg_max_temp=20.0,
            avg_min_temp=30.0,
            total_acc_ppt=10.0
        )
        response = self.client.get(reverse("stats-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)
        self.assertEqual(response.data["count"], 1)
