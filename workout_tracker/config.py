import os
from dotenv import load_dotenv

load_dotenv()

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
