import requests
from django.shortcuts import render

def get_weather_data(city):
    api_key = "61fda9b8c0e2d66a412039d5da16d4b8"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def weather_view(request):
    city = request.GET.get('city', 'Nairobi')
    weather_data = get_weather_data(city)
    context = {'weather': weather_data, 'city': city}
    return render(request, 'weather/weather.html', context)
