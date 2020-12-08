import requests
from django.shortcuts import render
from django.views.generic import View
from .models import City
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={API key}'
    cities = City.objects.all()

    data = []
    city = 'Las Vegas'
    cityweather = {}
    

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
