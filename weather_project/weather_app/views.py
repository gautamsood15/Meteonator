import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm, SearchForm
from django.http import HttpResponseRedirect

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=cee83e85f6aa300a481d0bc87650b513'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

        return HttpResponseRedirect("/")

    form = CityForm()


    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temprature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather_template.html', context)

    
def search(request):

    if request.method == 'POST':
        search_query = request.POST['name']
        print(search_query)


        return HttpResponseRedirect("/search")



    search_form = SearchForm()

    context = {'search_form' : search_form}
    return render(request, 'search_template.html', context)