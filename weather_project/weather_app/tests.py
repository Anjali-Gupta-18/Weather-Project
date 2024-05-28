from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import City, Weather
from unittest.mock import patch

class WeatherAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.city_name = "London"
        self.city = City.objects.create(name=self.city_name)
        self.weather = Weather.objects.create(
            city=self.city,
            temperature=20.0,
            description="clear sky"
        )

        response = self.client.post(reverse('home'), {'name': 'New York'})
        self.assertEqual(response.status_code, 302)  # Redirects after POST

        new_city = City.objects.get(name='New York')
        new_weather = Weather.objects.get(city=new_city)
        self.assertEqual(new_weather.temperature, 30.0)
        self.assertEqual(new_weather.description, 'hot')

