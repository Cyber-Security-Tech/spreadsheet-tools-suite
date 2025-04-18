"""
main.py — Entry point for the Habit Tracker tool

This CLI tool logs daily habits (e.g., minutes of study, workout, etc.)
using the Pixela API. It allows users to:
- Log today’s or custom-date habits
- Undo an entry
- View progress in the browser
- Retrieve today’s logged data

All configuration (API keys, graph IDs) is stored in .env via config.py.
"""

from habit_api import (
    log_habit,
    delete_habit,
    open_graph,
    select_graph,
    get_habit
)


def main():
    while True:
        print("\n📊 Habit Tracker Menu")
        print("1. Log today's habit")
        print("2. Log habit for a custom date")
        print("3. Undo today's entry")
        print("4. Open graph in browser")
        print("5. Exit")
        print("6. View today's logged minutes")

        choice = input("Choose an option (1–6): ")

        if choice == "1":
            graph_id = select_graph()
            minutes = input("How many minutes would you like to log today? ")
            if not minutes.isdigit():
                print("❌ Invalid input. Please enter a number.")
                continue
            log_habit(minutes, graph_id)

        elif choice == "2":
            graph_id = select_graph()
            raw_date = input("Enter date (YYYYMMDD or YYYY-MM-DD or YYYY/MM/DD): ").replace("-", "").replace("/", "")
            if len(raw_date) != 8 or not raw_date.isdigit():
                print("❌ Invalid date format. Please enter date as YYYYMMDD, YYYY-MM-DD, or YYYY/MM/DD.")
                continue
            minutes = input("How many minutes did you do on that day? ")
            if not minutes.isdigit():
                print("❌ Invalid input. Please enter a number.")
                continue
            log_habit(minutes, graph_id, raw_date)

        elif choice == "3":
            graph_id = select_graph()
            delete_habit(graph_id)

        elif choice == "4":
            graph_id = select_graph()
            open_graph(graph_id)

        elif choice == "5":
            print("👋 Goodbye!")
            break

        elif choice == "6":
            graph_id = select_graph()
            get_habit(graph_id)

        else:
            print("❌ Invalid choice. Please enter 1–6.")


if __name__ == "__main__":
    main()
