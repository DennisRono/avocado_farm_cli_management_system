# Weather Data Integration (stub function)
def view_weather_data():
    weather = {"Temperature": "25°C", "Precipitation": "10mm", "Humidity": "75%"}
    print("Weather forecast for today:")
    for key, value in weather.items():
        print(f"{key}: {value}")
