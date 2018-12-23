from django import forms
from .models import City

class CityForm(forms.ModelForm):

    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter city name...',
            'style': 'border-radius: 4px;',
        }
    ), )

    class Meta:
        model = City
        fields = [
            'name',
        ]
