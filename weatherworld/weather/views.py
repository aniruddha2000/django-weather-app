from django.views.generic import View
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm



class WeatherIndex(View):

    template_name = 'weather/city_create.html'


    def get(self, request):
        form = CityForm
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


    def post(self, request):
        form = CityForm(request.POST)

        if form.is_valid():
            form.save()

        api_key = "368a136ce5d41f1d9c904c8201b2d4b5"
        cities = City.objects.all()
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + api_key
        weather_data = []
        for city in cities:
            city_weather = requests.get(url.format(city)).json()
            weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }

            weather_data.append(weather)
        form = CityForm
        context = {
            'weather_data': weather_data,
            'form': form
        }
        return render(request, self.template_name, context)
