# ============================================
# Basic Weather App
# Beginner Tier - Oasis Infobyte SIP
# ============================================

import requests

# Paste your OpenWeather API key here
API_KEY = "6e6a0a4e945bcc31fb92d92a09080bbd"

print("===================================")
print("        BASIC WEATHER APP")
print("===================================")

while True:
    city = input("\nEnter city name: ").strip()

    if city == "":
        print("Error: Please enter a city name.")
        continue

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:

            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["main"]

            print("\n========== WEATHER ==========")
            print(f"City: {city_name}, {country}")
            print(f"Temperature: {temperature}°C")
            print(f"Weather: {weather}")
            print(f"Humidity: {humidity}%")
            print("=============================")

        else:
            print("\nRequest failed!")
            print("Status Code:", response.status_code)
            print("Response:", data)

    except requests.exceptions.RequestException:
        print("\nError: Unable to connect to the weather service.")

    again = input("\nSearch another city? (Y/N): ").strip().lower()

    if again == "n":
        print("\nThank you for using the Weather App!")
        break
    elif again != "y":
        print("\nInvalid choice. Exiting program.")
        break