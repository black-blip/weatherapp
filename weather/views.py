from django.shortcuts import render
import requests
from .models import City


def index(request):
    return render(request,'weather/index.html')


def search(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"
    context = {}
    if 'search' in request.GET:
        city = request.GET.get('search')
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city':city,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
            'feels_like': r['main']['feels_like'],
            'min_temp':r['main']['temp_min'],
            'max_temp':r['main']['temp_max'],
            'humidity':r['main']['humidity'],

        }

        context = {'city_weather':city_weather}

    return render(request,'weather/index.html',context)