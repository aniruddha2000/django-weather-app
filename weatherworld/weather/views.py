from django.views.generic import View
from .models import City
from .forms import CityForm
import requests
from django.shortcuts import render

class WeatherIndex(View):

    template_name = 'weather/city_create.html'


    def get(self, request, *args, **kwargs):
        cities = City.objects.all()
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9442c7cf14667f27786f5f4c023707c8'
        weather_data = []
        for city in cities:
            city_weather = request.get(url.format(city)).json()
            weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }

            weather_data.append(weather)
        context = {'weather_data': weather_data}
        return  render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = CityForm(request.POST)

        if form.is_valid():
            form.save()

        context = {'form': form}
        return render(request, self.template_name, context)