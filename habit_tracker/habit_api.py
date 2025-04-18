"""
habit_api.py — API interface for Pixela-based habit tracking

This module provides helper functions to:
- Log habits to a specific graph
- Delete entries
- View graphs in browser
- Retrieve data from a specific day

Graphs and credentials are defined in config.py.
"""

import requests
from datetime import datetime
import webbrowser
from config import USERNAME, TOKEN

# Define available graphs (graph_id, readable name)
GRAPH_IDS = {
    "1": ("tracker1", "Productivity"),
    "2": ("tracker2", "Workout")
}

BASE_URL = "https://pixe.la/v1/users"


def select_graph() -> str:
    """
    Prompts user to choose a graph and returns the graph_id.
    Defaults to the first graph if input is invalid.
    """
    print("\nSelect a graph:")
    for key, (_, name) in GRAPH_IDS.items():
        print(f"{key}. {name}")
    choice = input("Choose a graph: ")
    return GRAPH_IDS.get(choice, GRAPH_IDS["1"])[0]


def log_habit(quantity: str, graph_id: str, date: str = None) -> None:
    """
    Logs a new habit entry to the given graph.

    Args:
        quantity (str): Number of minutes to log
        graph_id (str): The Pixela graph ID
        date (str, optional): Date in YYYYMMDD format. Defaults to today.
    """
    date = date or datetime.now().strftime("%Y%m%d")
    url = f"{BASE_URL}/{USERNAME}/graphs/{graph_id}"
    data = {"date": date, "quantity": quantity}
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200 and response.json().get("isSuccess"):
        readable_date = datetime.strptime(date, "%Y%m%d").strftime("%B %d, %Y")
        print(f"Logged {quantity} minutes to '{graph_id}' for {readable_date}.")
    else:
        print(f"[ERROR] Failed to log habit: {response.json().get('message')}")


def delete_habit(graph_id: str, date: str = None) -> None:
    """
    Deletes the habit entry for the given date (default today).

    Args:
        graph_id (str): The Pixela graph ID
        date (str, optional): Date in YYYYMMDD format. Defaults to today.
    """
    date = date or datetime.now().strftime("%Y%m%d")
    url = f"{BASE_URL}/{USERNAME}/graphs/{graph_id}/{date}"
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.delete(url, headers=headers)

    if response.status_code == 200 and response.json().get("isSuccess"):
        print("Successfully deleted the entry.")
    else:
        print(f"[ERROR] Failed to delete entry: {response.json().get('message')}")


def open_graph(graph_id: str) -> None:
    """
    Opens the graph page in the user's browser.

    Args:
        graph_id (str): The Pixela graph ID
    """
    url = f"{BASE_URL}/{USERNAME}/graphs/{graph_id}.html"
    webbrowser.open(url)
    print(f"Opened '{graph_id}' in your browser.")


def get_habit(graph_id: str, date: str = None) -> None:
    """
    Retrieves the habit data for the given date (default today).

    Args:
        graph_id (str): The Pixela graph ID
        date (str, optional): Date in YYYYMMDD format. Defaults to today.
    """
    date = date or datetime.now().strftime("%Y%m%d")
    url = f"{BASE_URL}/{USERNAME}/graphs/{graph_id}/{date}"
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        quantity = response.json().get("quantity")
        readable_date = datetime.strptime(date, "%Y%m%d").strftime("%B %d, %Y")
        print(f"On {readable_date}, you logged {quantity} minutes to '{graph_id}'.")
    else:
        print(f"[ERROR] Could not retrieve data: {response.json().get('message')}")
