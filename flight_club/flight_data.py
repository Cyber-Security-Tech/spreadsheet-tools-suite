"""
🛫 flight_data.py — FlightData class

A simple data structure to represent a flight deal returned from the search API.
Stores all key flight details used for display and notification purposes.
"""

class FlightData:
    """
    Represents a flight deal with all relevant metadata.
    
    Attributes:
        price (int): Flight price in USD
        origin_city (str): Departure city name (e.g., "Washington D.C.")
        origin_airport (str): Departure IATA airport code (e.g., "IAD")
        destination_city (str): Destination city name (e.g., "Paris")
        destination_airport (str): Destination IATA airport code (e.g., "CDG")
        departure_date (str): Outbound flight date (YYYY-MM-DD)
        return_date (str): Return flight date (YYYY-MM-DD)
    """

    def __init__(
        self,
        price: int,
        origin_city: str,
        origin_airport: str,
        destination_city: str,
        destination_airport: str,
        departure_date: str,
        return_date: str
    ):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date

    def __repr__(self):
        return (
            f"<Flight {self.origin_airport} → {self.destination_airport} | "
            f"${self.price} | {self.departure_date} → {self.return_date}>"
        )
