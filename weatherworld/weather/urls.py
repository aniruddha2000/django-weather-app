from django.conf.urls import url
from django.urls import path
from .views import *

app_name = 'weatherApp'
urlpatterns = [
    url(r'^$', WeatherIndex.as_view(), name='index'),
    path('delete/<slug:pk>', WeatherDeleteView.as_view(), name='delete'),
    # url(r'^delete/(<pk>[0-9]+)/$', WeatherDeleteView.as_view(), name='delete'),
]