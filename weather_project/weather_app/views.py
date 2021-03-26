import requests
from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=cee83e85f6aa300a481d0bc87650b513'
    city = 'Las Vegas'

    r = requests.get(url.format(city))
    print(r.text)



    return render(request, 'weather_template.html')

    
