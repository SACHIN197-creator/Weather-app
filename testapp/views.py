import requests
from django.shortcuts import render
from testapp.forms import WeatherForm
from testapp.models import Weather


API_KEY = "124f8224105198bc21b17d40e40cd125"

def home(request):
    data = None
    form = WeatherForm()
    if request.method == "POST":
        form = WeatherForm(request.POST)
        if form.is_valid():
            form.save()
            city = form.cleaned_data['city']
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            weather = response.json()

            print(weather)
            if weather.get("cod") == 200:

                data = {
                    'city': weather['name'],

                    'temperature': weather['main']['temp'],

                    'description': weather['weather'][0]['description'],

                    'humidity': weather['main']['humidity'],

                    'wind': weather['wind']['speed'],
                }

            else:
                data = {

                    'error': weather.get("message")
                }

    return render(request,'testapp/weather.html',{ 'form': form,'data': data, })

# CURRENT LOCATION VIEW

def location_weather(request):
    data = None
    form = WeatherForm()

    # FROM CURRENT LOCATION PAGE
    # SEARCH ANOTHER CITY

    if request.method == "POST":
        form = WeatherForm(request.POST)
        if form.is_valid():
            form.save()
            city = form.cleaned_data['city']
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            weather = response.json()
            print(weather)
            if weather.get("cod") == 200:
                data = {

                    'city': weather['name'],

                    'temperature': weather['main']['temp'],

                    'description': weather['weather'][0]['description'],

                    'humidity': weather['main']['humidity'],

                    'wind': weather['wind']['speed'],
                }
            else:
                data = {

                    'error': weather.get("message")
                }

    # CURRENT LOCATION WEATHER

    else:
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        weather = response.json()
        print(weather)
        if weather.get("cod") == 200:

            data = {

                'city': weather['name'],

                'temperature': weather['main']['temp'],

                'description': weather['weather'][0]['description'],

                'humidity': weather['main']['humidity'],

                'wind': weather['wind']['speed'],
            }

        else:

            data = {

                'error': weather.get("message")
            }

    return render(request,'testapp/weather.html',{ 'form': form,'data': data, })