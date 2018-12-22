from django.db import models
from django.urls import reverse

class City(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('weatherApp:index')
