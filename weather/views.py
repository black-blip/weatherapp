import requests
from django.shortcuts import render
from django.views.generic import View
from .models import City
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=67202aa61e9bebd603b24c7514ea3098'
    cities = City.objects.all()

    data = []
    city = 'Las Vegas'
    for city in cities:

        r = requests.get(url.format(city)).json()
        cityweather = {
            'city':city,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        data.append(cityweather)
        

    context = {
        'cityweather': cityweather
    }


    return render(request,'weather/index.html',context)