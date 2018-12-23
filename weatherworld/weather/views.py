from django.views.generic import View
from .models import City
from .forms import CityForm
import requests
from django.shortcuts import render

class WeatherIndex(View):

    template_name = 'weather/city_create.html'


    def get(self, request):
        cities = City.objects.all()
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=368a136ce5d41f1d9c904c8201b2d4b5'
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
        context = {'weather_data': weather_data}
        return  render(request, self.template_name, context)


    def post(self, request):
        form = CityForm(request.POST)

        if form.is_valid():
            form.save()

        context = {'form': form}
        return render(request, self.template_name, context)