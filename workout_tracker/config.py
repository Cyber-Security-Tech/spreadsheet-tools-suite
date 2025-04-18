"""
config.py — Loads environment variables for the Workout Tracker

This module securely loads the following credentials from a .env file:

- NUTRITIONIX_APP_ID: App ID for Nutritionix API
- NUTRITIONIX_API_KEY: API key for Nutritionix workout parsing
- SHEETY_ENDPOINT: API URL for logging data to Google Sheets
"""

import os
from dotenv import load_dotenv

load_dotenv()

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
