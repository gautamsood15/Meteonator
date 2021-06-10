from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=cee83e85f6aa300a481d0bc87650b513'
    return render(request, 'weather_template.html')

    
