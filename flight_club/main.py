"""
📍 main.py — Entry Point for Flight Club

This script checks for cheap flights from a fixed origin airport to various destinations 
listed in a Google Sheet. If a matching flight under the budget is found, it sends an 
email alert to the user.

Usage:
- Toggle DEMO_MODE = True to showcase mock data (for portfolio/demo use)
- Set DEMO_MODE = False to enable real-time flight search and notifications
- Requires API keys and configuration in a .env file:
    ORIGIN_CITY=IAD

Modules:
- DataManager: Handles Google Sheets integration
- FlightSearch: Searches for flights via API
- FlightData: Data class for flight info
- NotificationManager: Sends email alerts when a deal is found
"""

import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

# Load environment variables
load_dotenv()
ORIGIN_CITY = os.getenv("ORIGIN_CITY", "IAD")

# Toggle to True for demo mode
DEMO_MODE = True


def display_flight_info(flight: FlightData):
    """Prints formatted flight information to console."""
    print("✅ CHEAP FLIGHT FOUND!")
    print(f"{flight.origin_city} ({flight.origin_airport}) → {flight.destination_city} ({flight.destination_airport})")
    print(f"Price: ${flight.price}")
    print(f"Departure: {flight.departure_date} | Return: {flight.return_date}")


if DEMO_MODE:
    print("\n🎓 DEMO MODE ENABLED – Running with mock data only\n")

    # Mock flight for demonstration purposes
    mock_flight = FlightData(
        price=199,
        origin_city=ORIGIN_CITY,
        origin_airport=ORIGIN_CITY,
        destination_city="Paris",
        destination_airport="CDG",
        departure_date="2025-06-01",
        return_date="2025-06-08"
    )

    display_flight_info(mock_flight)

else:
    print(f"\n🚀 Starting flight search from origin: {ORIGIN_CITY}")
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    # Load spreadsheet data
    sheet_data = data_manager.get_destination_data()

    for destination in sheet_data:
        dest_code = destination["iataCode"]
        max_price = destination["lowestPrice"]
        city_name = destination["city"]

        print(f"\n🔍 Searching: {ORIGIN_CITY} → {dest_code} | Max Price: ${max_price}")

        # Search for flights to this destination
        flight = flight_search.search_flights(
            origin_city=ORIGIN_CITY,
            destination_city=dest_code,
            max_price=max_price
        )

        if flight:
            display_flight_info(flight)
            notification_manager.send_email(flight)
        else:
            print("❌ No deals found within budget.")
