## Weather App

 A simple Django-based weather application that fetches weather data from OpenWeatherMap API and displays it using Django templates.

## Features

- Search weather by city

- Display current temperature and weather conditions

- Minimalist UI

- Uses OpenWeatherMap API


## Installation

1. Clone the Repository

        git clone https://github.com/amohnice/weather_project.git
        cd weather-app

2. Create and Activate a Virtual Environment

       python -m venv venv
       source venv/bin/activate  # On Windows use venv\Scripts\activate

3. Install Dependencies

       pip install -r requirements.txt

4. Set Up Environment Variables

 Create a .env file in the root directory and add:

        OPENWEATHERMAP_API_KEY=your_actual_api_key_here

5. Run Migrations

        python manage.py migrate

6. Run the Server

        python manage.py runserver

## Usage

1. Open a browser and go to http://127.0.0.1:8000/


2. Enter a city name in the search bar


3. View the current weather and conditions


## Folder Structure

weather_project/
│── weather/
│   ├── templates/
│   │   ├── weather/
│   │   │   ├── weather.html
│   ├── views.py
│   ├── urls.py
│── weather_project/
│── .env
│── manage.py
│── requirements.txt

