from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import City, Weather
from .forms import CityForm

def fetch_weather_data(city_name):
    api_key = '858f15fed9292cbe25c341a754c55e45'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    # url = f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}'

    
    # url = f'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    return None

def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            weather_data = fetch_weather_data(city_name)
            if weather_data:
                city, created = City.objects.get_or_create(name=city_name)
                Weather.objects.update_or_create(
                    city=city,
                    defaults={
                        'temperature': weather_data['temperature'],
                        'description': weather_data['description'],
                        'last_updated': timezone.now()
                    }
                )
            return redirect('home')
    else:
        form = CityForm()

    weather_info = Weather.objects.all()
    return render(request, 'home.html', {'form': form, 'weather_info': weather_info})
