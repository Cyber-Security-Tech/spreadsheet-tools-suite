import requests
from datetime import datetime
from config import NUTRITIONIX_APP_ID, NUTRITIONIX_API_KEY, SHEETY_ENDPOINT

DEMO_MODE = True  # Toggle this in main.py

def parse_workout(user_input):
    if DEMO_MODE:
        return [
            {"name": "Running", "duration_min": 30, "nf_calories": 250},
            {"name": "Yoga", "duration_min": 20, "nf_calories": 90},
        ]
    
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
        "Content-Type": "application/json"
    }
    params = {
        "query": user_input,
        "gender": "female",
        "weight_kg": 65,
        "height_cm": 170,
        "age": 25
    }

    response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=params, headers=headers)
    response.raise_for_status()
    return response.json()["exercises"]

def log_to_sheet(exercises):
    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%H:%M:%S")

    for exercise in exercises:
        sheet_input = {
            "workout": {
                "date": today,
                "time": now,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        response = requests.post(SHEETY_ENDPOINT, json=sheet_input)
        response.raise_for_status()
