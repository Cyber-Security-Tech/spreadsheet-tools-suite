"""
flight_search.py — Handles communication with the Amadeus API

Provides methods to:
- Get the IATA code for a city
- Search for flights within a given price threshold
"""

import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from amadeus import Client, ResponseError
from flight_data import FlightData

load_dotenv()


class FlightSearch:
    """
    A class to interact with the Amadeus API for flight data retrieval.
    """

    def __init__(self):
        self.amadeus = Client(
            client_id=os.getenv("AMADEUS_CLIENT_ID"),
            client_secret=os.getenv("AMADEUS_CLIENT_SECRET")
        )

    def get_iata_code(self, city_name: str) -> str | None:
        """
        Retrieves the IATA airport code for a given city.

        Args:
            city_name (str): The name of the city to look up.

        Returns:
            str or None: The IATA code, or None if not found.
        """
        try:
            response = self.amadeus.reference_data.locations.get(
                keyword=city_name,
                subType='CITY'
            )
            if response.data:
                return response.data[0]["iataCode"]
            else:
                print(f"[INFO] No IATA code found for city: {city_name}")
                return None
        except ResponseError as error:
            print(f"[ERROR] Amadeus API error while fetching IATA code: {error}")
            return None

    def search_flights(self, origin_city: str, destination_city: str, max_price: float) -> FlightData | None:
        """
        Searches for the cheapest round-trip flight from origin to destination within the price limit.

        Args:
            origin_city (str): IATA code of the departure city.
            destination_city (str): IATA code of the destination city.
            max_price (float): Maximum acceptable price for the flight.

        Returns:
            FlightData or None: A FlightData object if a deal is found, otherwise None.
        """
        date_from = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        date_to = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')

        try:
            response = self.amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin_city,
                destinationLocationCode=destination_city,
                departureDate=date_from,
                returnDate=date_to,
                adults=1,
                max=1
            )

            if not response.data:
                print(f"[INFO] No flight deals found for {origin_city} → {destination_city}")
                return None

            offer = response.data[0]
            price = float(offer["price"]["total"])

            if price <= max_price:
                itinerary = offer["itineraries"][0]["segments"][0]
                return_itinerary = offer["itineraries"][1]["segments"][0]

                return FlightData(
                    price=price,
                    origin_city=origin_city,
                    origin_airport=itinerary["departure"]["iataCode"],
                    destination_city=destination_city,
                    destination_airport=itinerary["arrival"]["iataCode"],
                    departure_date=itinerary["departure"]["at"].split("T")[0],
                    return_date=return_itinerary["arrival"]["at"].split("T")[0]
                )

        except ResponseError as error:
            print(f"[ERROR] Amadeus API error during flight search: {error}")

        return None
