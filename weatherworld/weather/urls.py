from django.conf.urls import url
from .views import *

app_name = 'weatherApp'
urlpatterns = [
    url(r'^$', Weatherindex.as_view(), name='index'),
]