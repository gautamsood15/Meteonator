import requests
from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=cee83e85f6aa300a481d0bc87650b513'
    city = ''

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temprature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    context = {'city_weather' : city_weather}
    return render(request, 'weather_template.html', context)

    
