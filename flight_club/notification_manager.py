"""
notification_manager.py — Sends email alerts for flight deals.

This class connects to an SMTP server and sends a formatted email 
containing flight deal details.

Configuration:
- Requires MY_EMAIL and MY_EMAIL_PASSWORD in a .env file.
- Uses Gmail SMTP on port 587 with TLS.
"""

import os
import smtplib
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()


class NotificationManager:
    """
    Handles sending email notifications with flight deal information.
    """

    def __init__(self):
        self.email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_EMAIL_PASSWORD")

    def send_email(self, flight_data: FlightData, to_address: str = None):
        """
        Sends an email alert with the flight details.

        Args:
            flight_data (FlightData): The flight deal to include in the email.
            to_address (str, optional): Destination email. Defaults to sender's email.
        """
        to_address = to_address or self.email

        subject = f"Low price alert! Only ${flight_data.price} to {flight_data.destination_city}"
        body = (
            f"Cheap flight found!\n\n"
            f"{flight_data.origin_city} ({flight_data.origin_airport}) → "
            f"{flight_data.destination_city} ({flight_data.destination_airport})\n"
            f"Price: ${flight_data.price}\n"
            f"From {flight_data.departure_date} to {flight_data.return_date}"
        )
        message = f"Subject: {subject}\n\n{body}"

        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.password)
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=to_address,
                    msg=message.encode('utf-8')
                )
                print(f"[INFO] Email sent to {to_address}")
        except smtplib.SMTPException as error:
            print(f"[ERROR] Failed to send email: {error}")
