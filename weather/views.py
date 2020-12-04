import requests
from django.shortcuts import render
from django.views.generic import View
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={API key}'
    city = 'Denver'
    r = requests.get(url.format(city)).json()
    weather = {
        'city':city,
        'temperature':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }

    context = {
        'weather': weather
    }

    return render(request,'weather/index.html',context)