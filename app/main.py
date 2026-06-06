from fastapi import FastAPI
from app.controllers.weather_controller import get_weather

app = FastAPI(title="Weather AI Production Service")

@app.get("/")
def home():
    return {"message": "Weather AI Service Running"}

@app.get("/weather")
def weather(city: str):
    return get_weather(city)
