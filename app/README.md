# Weather AI Service

A FastAPI-based weather intelligence service that consumes real-time weather data from OpenWeather and generates AI-style weather insights and recommendations. The service is deployed on Render and exposes a public REST API.

## Features

- Real-time weather data retrieval by city
- AI-style weather recommendations and insights
- In-memory caching for improved performance
- FastAPI REST API
- Environment variable configuration
- Production-ready structure
- Cloud deployment support (Render)

## Project Structure

app/
├── controllers/
├── services/
├── utils/
├── main.py
├── config.py
└── __init__.py

## Installation

Clone the repository:
git clone https://github.com/makaz521/weather-ai-service.git
cd weather-ai-service

Install dependencies:
python -m pip install -r requirements.txt

Create a .env file:
OPENWEATHER_API_KEY=your_api_key_here

Run the application:
python -m uvicorn app.main:app --reload

Server runs at:
http://127.0.0.1:8000

## API Endpoints

Home:
GET /

Response:
{
  "message": "Weather AI Service Running"
}

Weather:
GET /weather?city=Nairobi

Example response:
{
  "city": "Nairobi",
  "temperature": 16.6,
  "humidity": 87,
  "condition": "overcast clouds",
  "insight": "Weather feels cool with humid conditions. Light jacket recommended."
}

## Technology Stack

- Python
- FastAPI
- OpenWeather API
- HTTPX
- SlowAPI

## Deployment

Live on Render:
https://weather-ai-service-o5f4.onrender.com

## Author

Dennis Muema
GitHub: https://github.com/makaz521