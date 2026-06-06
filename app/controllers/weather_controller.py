from app.services.weather_service import fetch_weather
from app.utils.ai_engine import generate_insight

def get_weather(city: str):

    data = fetch_weather(city)

    if not data:
        return {"error": "Unable to fetch weather data"}

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    return {
        "city": data["name"],
        "temperature": temp,
        "humidity": humidity,
        "condition": condition,
        "insight": generate_insight(temp, humidity, condition)
    }