import requests

API_KEY = '30d39436166cb37ff65b03ce9bfdf90e'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

city_name = input("Enter city name: ")

complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}"

response = requests.get(complete_url)
data = response.json()

if data['cod'] == 200:
    main_data = data['main']
    weather_data = data['weather'][0]

    temperature = main_data['temp']
    humidity = main_data['humidity']
    description = weather_data['description']

    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description.capitalize()}")
else:
    print("City not found")
    
response = requests.get(complete_url)

if response.status_code == 200:
    data = response.json()
    main_data = data['main']
    weather_data = data['weather'][0]
    # Existing code to extract and display weather data
else:
    print("Error fetching weather data. Please check your input or try again later.")

if response.status_code == 200:
    data = response.json()
    main_data = data['main']
    weather_data = data['weather'][0]

    wind_speed = data['wind']['speed']
    visibility = data['visibility']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']

    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Visibility: {visibility} meters")
   

    # Existing code to display temperature, humidity, and description
import tkinter as tk
import requests
from datetime import datetime
from tkinter import messagebox

def fetch_weather():
    city_name = city_entry.get()
    complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main_data = data['main']
        weather_data = data['weather'][0]

        wind_speed = data['wind']['speed']
        visibility = data['visibility']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']

        info = f"Temperature: {main_data['temp']} K\n"
        info += f"Humidity: {main_data['humidity']}%\n"
        info += f"Description: {weather_data['description'].capitalize()}\n"
        info += f"Wind Speed: {wind_speed} m/s\n"
        info += f"Visibility: {visibility} meters\n"
        info += f"Sunrise: {datetime.utcfromtimestamp(sunrise).strftime('%Y-%m-%d %H:%M:%S')}\n"
        info += f"Sunset: {datetime.utcfromtimestamp(sunset).strftime('%Y-%m-%d %H:%M:%S')}"

        result_label.config(text=info)
    else:
        messagebox.showerror("Error", "Unable to fetch weather data. Please check your input or try again later.")

app = tk.Tk()
app.title("Weather App")

city_label = tk.Label(app, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

fetch_button = tk.Button(app, text="Fetch Weather", command=fetch_weather)
fetch_button.pack()

result_label = tk.Label(app, text="", justify="left")
result_label.pack()

app.mainloop()
