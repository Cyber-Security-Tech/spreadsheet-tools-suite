"""
main.py — Entry point for the Workout Tracker tool

This script uses natural language input to log workouts, parses them
using the Nutritionix API, and stores them in a Google Sheet via Sheety.

Usage:
- Enter a workout in plain English (e.g. "ran 3 miles and did 20 min yoga")
- Parsed exercises are printed and logged
- Supports demo mode (toggle DEMO_MODE = True)

APIs:
- Nutritionix for parsing workouts
- Sheety for logging to Google Sheets
"""

from workout_api import parse_workout, log_to_sheet

# Toggle this to True for demo/testing mode
DEMO_MODE = True

def main():
    print("🏋️ Workout Tracker\n")
    user_input = input("What workout did you do? (e.g. 'ran 3 miles and did 20 min yoga')\n> ")

    try:
        exercises = parse_workout(user_input)
        print("\n📝 Workout summary:")
        for ex in exercises:
            print(f"- {ex['name'].title()}: {ex['duration_min']} min | {ex['nf_calories']} cal")

        log_to_sheet(exercises)
        print("\n✅ Workout logged to Google Sheet.")
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")

if __name__ == "__main__":
    main()
