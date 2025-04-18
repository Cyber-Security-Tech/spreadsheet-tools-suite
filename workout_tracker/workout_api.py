"""
workout_api.py — Handles workout parsing and logging

This module:
- Parses natural-language workout input using the Nutritionix API
- Logs workout data to a Google Sheet using the Sheety API
- Supports demo mode for recruiter/testing scenarios
"""

import requests
from datetime import datetime
from config import NUTRITIONIX_APP_ID, NUTRITIONIX_API_KEY, SHEETY_ENDPOINT

# Toggle demo mode in main.py
DEMO_MODE = True


def parse_workout(user_input: str) -> list[dict]:
    """
    Sends workout input to the Nutritionix API and returns a list of exercises.

    Args:
        user_input (str): Natural language input describing the workout

    Returns:
        list of dict: Parsed exercises with name, duration, and calories
    """
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
        "gender": "female",  # You could optionally load these from .env or ask the user
        "weight_kg": 65,
        "height_cm": 170,
        "age": 25
    }

    response = requests.post(
        url="https://trackapi.nutritionix.com/v2/natural/exercise",
        json=params,
        headers=headers
    )
    response.raise_for_status()
    return response.json()["exercises"]


def log_to_sheet(exercises: list[dict]) -> None:
    """
    Logs each exercise to the Google Sheet via Sheety.

    Args:
        exercises (list of dict): List of parsed exercises to log
    """
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
