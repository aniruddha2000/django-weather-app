from django.shortcuts import render
from django.views.generic import ListView
from .models import City

class Weatherindex(ListView):

    template_name = 'weather/city_list.html'
    queryset = City.objects.all()