# 🏋️ Workout Tracker

A Python tool that tracks your workouts using natural language input and logs them to Google Sheets using the Sheety API. Supports both real and demo modes for easy testing without API setup.

## 🚀 Demo Mode Included

Recruiters or reviewers can test the app **without any API keys** by toggling demo mode in `main.py`:

```python
DEMO_MODE = True
```

This simulates realistic output and logs mock data to your connected Google Sheet.

---

## 🔧 Features

- ✅ Parse workout descriptions with Nutritionix API (demo mode simulates it)
- ✅ Logs workout data (exercise, duration, calories) to Google Sheets via Sheety
- ✅ Supports real mode for full integration
- ✅ Secure `.env` usage with `.env.example` provided
- ✅ Clean, modular Python codebase

---

## 📂 Project Structure

```
workout_tracker/
│
├── main.py           # CLI interface, handles user interaction
├── workout_api.py    # Logic for API call or mock response, logs to sheet
├── config.py         # Loads .env values securely
├── .env.example      # Template for required environment variables
├── requirements.txt  # Dependencies
└── README.md         # Project overview and usage
```

---

## 🔒 Environment Variables

```
NUTRITIONIX_APP_ID=your_app_id_here
NUTRITIONIX_API_KEY=your_api_key_here
SHEETY_ENDPOINT=https://api.sheety.co/your_endpoint_here
```

---

## 📊 Sample Output

```text
What workout did you do?
> ran 3 miles and did 20 min yoga

Workout summary:
- Running: 30 min | 250 cal
- Yoga: 20 min | 90 cal

✅ Workout logged to Google Sheet.
```

---

## 💡 What I Learned

- Working with external APIs (Nutritionix, Sheety)
- Handling user input and simulating responses
- Data formatting and API automation with Google Sheets
- Creating modular, scalable CLI tools with real/demo modes
