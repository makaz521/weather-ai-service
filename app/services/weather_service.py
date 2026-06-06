import requests
from app.config import API_KEY, BASE_URL

# Simple in-memory cache
cache = {}

def fetch_weather(city: str):

    # 1. Check cache first (fast response)
    if city in cache:
        print("CACHE HIT:", city)
        return cache[city]

    # 2. API request params
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    # 3. Call OpenWeather API
    response = requests.get(BASE_URL, params=params)

    # 4. Handle failure
    if response.status_code != 200:
        print("API ERROR:", response.text)
        return None

    # 5. Convert response
    data = response.json()

    # 6. Store in cache
    cache[city] = data

    return data