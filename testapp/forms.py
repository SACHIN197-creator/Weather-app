from django import forms
from .models import Weather

class WeatherForm(forms.ModelForm):

    class Meta:

        model = Weather

        fields = ['city']

        widgets = {
            'city': forms.TextInput(attrs={
                'placeholder':'Enter City Name',
                'class':'form-control'
            })
        }