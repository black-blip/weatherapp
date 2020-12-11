from django.shortcuts import render
import requests
from .models import City

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=67202aa61e9bebd603b24c7514ea3098'
    city = 'London'
    cities = City.objects.all()

    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city':city.name,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }

        weather_data.append(city_weather)
    
    context = {'weather_data':weather_data}

    return render(request,'weather/index.html',context)


def search(request):

    return render(request,'weather/index.html')