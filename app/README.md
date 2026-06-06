# Weather AI Service

A FastAPI-based weather intelligence service that consumes weather data from OpenWeather and generates AI-style weather insights.

## Features

- Real-time weather data retrieval
- AI-style weather recommendations
- In-memory caching for improved performance
- FastAPI REST API
- Environment variable configuration
- Production-ready structure

## Project Structure

```
app/
├── controllers/
├── services/
├── utils/
├── main.py
├── config.py
└── __init__.py
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd weather-ai-service
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

### Run Application

```bash
python -m uvicorn app.main:app --reload
```

## API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "Weather AI Service Running"
}
```

### Weather

```http
GET /weather?city=Nairobi
```

Example Response:

```json
{
  "city": "Nairobi",
  "temperature": 16.6,
  "humidity": 87,
  "condition": "overcast clouds",
  "insight": "Weather feels cool with humid conditions. Current condition is overcast clouds. You should wear a light jacket and expect mild skies."
}
```

## Technology Stack

- Python
- FastAPI
- OpenWeather API
- HTTPX
- SlowAPI

## Deployment

Designed for deployment on Render.

## Author

Dennis Makau