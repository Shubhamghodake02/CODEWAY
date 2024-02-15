import requests

def get_weather_data(location):
    # Enter your OpenWeatherMap API key here
    api_key = "YOUR_API_KEY"

    # Construct the API URL based on the user's input
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    # Send an HTTP request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract relevant weather information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        return {
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'description': description
        }
    else:
        # Return None if request failed
        return None

def display_weather(weather_data, location):
    if weather_data:
        print(f"Weather in {location}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
        print(f"Description: {weather_data['description']}")
    else:
        print("Error retrieving weather data. Please check your input.")

def main():
    location = input("Enter the name of a city or a zip code: ")

    weather_data = get_weather_data(location)

    display_weather(weather_data, location)

if __name__ == "__main__":
    main()
