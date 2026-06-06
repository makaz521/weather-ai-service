import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

API_KEY = os.getenv("OPENWEATHER_API_KEY")

print("API KEY LOADED:", API_KEY)


# ---------------- AI LAYER ----------------
def generate_weather_insight(temp, humidity, condition):

    if temp < 18:
        feeling = "cool"
    elif temp < 28:
        feeling = "mild"
    else:
        feeling = "hot"

    if humidity > 80:
        humidity_text = "high humidity"
    else:
        humidity_text = "moderate humidity"

    return (
        f"It is currently {feeling} at {temp}°C with {condition} and {humidity_text}. "
        f"Dress appropriately for the weather."
    )


# ---------------- MAIN FUNCTION ----------------
def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    return {
        "city": data["name"],
        "temperature": temp,
        "humidity": humidity,
        "condition": condition,
        "insight": generate_weather_insight(temp, humidity, condition)
    }