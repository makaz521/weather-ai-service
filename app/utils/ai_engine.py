def generate_insight(temp, humidity, condition):
    
    # Temperature reasoning
    if temp < 15:
        temp_desc = "very cold"
        advice = "wear heavy warm clothing"
    elif temp < 22:
        temp_desc = "cool"
        advice = "wear a light jacket"
    elif temp < 30:
        temp_desc = "warm"
        advice = "light clothing is fine"
    else:
        temp_desc = "hot"
        advice = "stay hydrated and avoid direct sun"

    # Humidity reasoning
    if humidity > 80:
        humidity_desc = "very humid"
    elif humidity > 60:
        humidity_desc = "humid"
    else:
        humidity_desc = "dry"

    # Condition reasoning
    condition = condition.lower()

    if "rain" in condition:
        weather_advice = "carry an umbrella"
    elif "cloud" in condition:
        weather_advice = "expect mild skies"
    elif "clear" in condition:
        weather_advice = "perfect outdoor weather"
    else:
        weather_advice = "normal conditions"

    return (
        f"Weather feels {temp_desc} with {humidity_desc} conditions. "
        f"Current condition is {condition}. "
        f"You should {advice} and {weather_advice}."
    )