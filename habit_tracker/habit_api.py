import requests
from datetime import datetime
<<<<<<< HEAD
import webbrowser
from config import USERNAME, TOKEN

GRAPH_IDS = {
    "1": ("tracker1", "Productivity"),
    "2": ("tracker2", "Workout")
}

def select_graph():
    print("\nSelect a graph:")
    for key, (_, name) in GRAPH_IDS.items():
        print(f"{key}. {name}")
    choice = input("Choose a graph: ")
    return GRAPH_IDS.get(choice, GRAPH_IDS["1"])[0]

def log_habit(quantity, graph_id, date=None):
    if not date:
        date = datetime.now().strftime("%Y%m%d")
    url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}"
    data = {"date": date, "quantity": quantity}
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200 and response.json().get("isSuccess"):
        readable_date = datetime.strptime(date, "%Y%m%d").strftime("%B %d, %Y")
        print(f"✅ Logged {quantity} minutes to {graph_id} for {readable_date}.")
    else:
        print(f"❌ Failed to log habit: {response.json().get('message')}")

def delete_habit(graph_id, date=None):
    if not date:
        date = datetime.now().strftime("%Y%m%d")
    url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}/{date}"
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.delete(url, headers=headers)

    if response.status_code == 200 and response.json().get("isSuccess"):
        print("🗑️ Successfully deleted today's entry.")
    else:
        print(f"❌ Failed to delete entry: {response.json().get('message')}")

def open_graph(graph_id):
    url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}.html"
    webbrowser.open(url)
    print(f"🌐 Opened {graph_id} in your browser.")

def get_habit(graph_id, date=None):
    if not date:
        date = datetime.now().strftime("%Y%m%d")
    url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}/{date}"
    headers = {"X-USER-TOKEN": TOKEN}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        quantity = response.json().get("quantity")
        readable_date = datetime.strptime(date, "%Y%m%d").strftime("%B %d, %Y")
        print(f"📅 On {readable_date}, you logged {quantity} minutes to {graph_id}.")
    else:
        print(f"❌ Could not retrieve habit data: {response.json().get('message')}")
=======
from config import USERNAME, TOKEN, GRAPH_ID

def log_habit(quantity):
    today = datetime.now().strftime("%Y%m%d")  
    post_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": today,
        "quantity": quantity
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(url=post_pixel_endpoint, json=pixel_data, headers=headers)
    print("Log Habit:", response.text)
>>>>>>> 296977a (Add Habit Tracker tool: Pixela API integration, .env config, and working habit logging with date fix)
