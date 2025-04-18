# 🏋️ Workout Tracker – Spreadsheet Tools Suite

A real-world Python project that transforms natural language workout descriptions into structured exercise logs using the Nutritionix API, then stores them in a Google Sheet via the Sheety API. Users can input workouts like "ran 3 miles and did 20 min yoga," and the program automatically parses and logs the data with calories burned and duration.

🧩 This is one of three tools in the **Spreadsheet Tools Suite**, a collection of real-world Python automation projects using Google Sheets and public APIs to build practical, portfolio-ready solutions.

---

## 🧪 Demo Mode Included

Recruiters and reviewers can test the tool without API setup by enabling demo mode in `main.py`:

```python
DEMO_MODE = True
```

This will simulate workout parsing and logging with mock data.

---

## 📸 Screenshot

<img src="media/screenshots/workout_demo.png" alt="Workout Tracker demo" width="600">

---

## 🚀 Features

- ✅ Accepts natural language workout input
- ✅ Parses workouts using Nutritionix API
- ✅ Displays exercise summary with duration and calories
- ✅ Logs workouts to Google Sheets via Sheety API
- ✅ Supports Demo Mode for easy testing
- ✅ Simple, clean CLI experience
- ✅ Secure `.env` usage with `.env.example` provided

---

## 🧰 Tech Stack

- **Python** – Core scripting language  
- **Nutritionix API** – Parses natural-language workouts  
- **Sheety API** – Logs structured data into Google Sheets  
- **Dotenv** – Manages environment variables securely  
- **Requests** – Handles HTTP requests

---

## 📂 Project Structure

```
workout_tracker/
├── main.py              # CLI entry point with demo mode toggle
├── workout_api.py       # Handles workout parsing and logging
├── config.py            # Loads API credentials from .env
├── .env.example         # Template for environment variables
├── .gitignore           # Ensures sensitive files and compiled code are ignored
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🔒 Environment Variables

Create a `.env` file in the root of `workout_tracker/` with:

```
NUTRITIONIX_APP_ID=your_app_id
NUTRITIONIX_API_KEY=your_api_key
SHEETY_ENDPOINT=https://api.sheety.co/your_sheet_endpoint
```

Use `.env.example` as a reference.

---

## 🧪 How to Run Locally

1. Clone the repo  
2. Add your `.env` file  
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python main.py
```

Or toggle `DEMO_MODE = True` for mock mode (no API calls needed).

---

## 💡 What I Learned

- Integrating multiple APIs (Nutritionix and Sheety)
- Structuring natural language into data-rich formats
- Creating clean CLI tools with flexible input handling
- Using .env files securely in production-ready code

---

## 🛠️ Future Improvements

- Add gender/weight/height input dynamically or via config  
- Support batch logging or editing past workouts  
- Add export options (CSV, PDF) for workout history  
- Convert to a Flask-based web app with charts and auth

---

## 👀 Why This Project Matters

This project blends:
- ✅ Real-world natural language processing  
- ✅ Useful automation for health tracking  
- ✅ Google Sheets integration  
- ✅ Clean CLI interaction  

It demonstrates the ability to turn user-friendly input into structured, persistent data — something valuable in both consumer tools and enterprise systems.
