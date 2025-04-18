"""
📦 data_manager.py — Manages communication with Google Sheet via Sheety API

This class fetches and updates destination data in the spreadsheet, particularly for:
- Getting all destination rows
- Updating missing IATA codes

Configuration:
- Requires SHEET_ENDPOINT in .env
- Optional: change SHEET_NAME if spreadsheet key differs (e.g., "prices", "sheet1")

Example data format expected:
[
    {
        "id": 1,
        "city": "Paris",
        "iataCode": "",
        "lowestPrice": 400
    },
    ...
]
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

# Customize if your sheet is named something else
SHEET_NAME = "sheet1"
DEBUG = False  # Set to True for verbose output


class DataManager:
    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        """Fetches the destination list from the spreadsheet."""
        response = requests.get(url=SHEET_ENDPOINT)
        response.raise_for_status()
        self.destination_data = response.json()[SHEET_NAME]
        return self.destination_data

    def update_iata_code(self, city_id, iata_code):
        """
        Updates the IATA code for a specific row in the spreadsheet.
        
        Args:
            city_id (int): The row ID to update
            iata_code (str): The IATA airport code (e.g., "CDG")
        """
        update_endpoint = f"{SHEET_ENDPOINT}/{city_id}"
        body = {
            SHEET_NAME: {
                "iataCode": iata_code
            }
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.put(url=update_endpoint, json=body, headers=headers)

        if DEBUG:
            print(f"\n📤 Updating city ID {city_id} with IATA code '{iata_code}'")
            print("Request body:", body)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)

        response.raise_for_status()
