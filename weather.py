import requests
from InquirerPy import prompt
from main import display_table


def get_coordinates(city_name):
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    response = requests.get(geocoding_url)

    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            location_data = data["results"][0]
            latitude = location_data["latitude"]
            longitude = location_data["longitude"]
            return latitude, longitude
        else:
            print(f"No results found for {city_name}.")
            return None
    else:
        print(f"Error: Unable to fetch data for {city_name}.")
        return None


def get_weather_forecast(latitude, longitude):
    forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m,dew_point_2m,precipitation_probability"
    response = requests.get(forecast_url)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(
            f"Error: Unable to fetch weather data for coordinates ({latitude}, {longitude})."
        )
        return None


def view_weather_data():
    questions = [
        {
            "type": "input",
            "name": "city",
            "message": "Enter Your Location Town Name:",
            "validate": lambda val: val.strip() != "" or "Location cannot be empty.",
        },
    ]
    answers = prompt(questions)
    city_name = answers["city"]
    coordinates = get_coordinates(city_name)
    if coordinates:
        latitude, longitude = coordinates
        print(
            f"Coordinates for {city_name}: Latitude = {latitude}, Longitude = {longitude}"
        )
        weather_forecast = get_weather_forecast(latitude, longitude)
        if weather_forecast:
            print("Weather forecast:")
            hourly_data = weather_forecast["hourly"]
            hours = len(hourly_data["temperature_2m"])
            data = []
            for hour in range(hours):
                row = [
                    f"Hour {hour + 1}",
                    f"{hourly_data['temperature_2m'][hour]}°C",
                    f"{hourly_data['relative_humidity_2m'][hour]}%",
                    f"{hourly_data['dew_point_2m'][hour]}°C",
                    f"{hourly_data['precipitation_probability'][hour]}%",
                ]
                data.append(row)

            headers = [
                "Time",
                "Temperature (2m)",
                "Relative Humidity (2m)",
                "Dew Point (2m)",
                "Precipitation Probability",
            ]

            display_table(data, headers)

    else:
        print("No valid coordinates found.")
