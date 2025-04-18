# 🧾 Spreadsheet Tools Suite

A professional collection of 3 automated Python tools that use real-world APIs, automation, and spreadsheet integration to solve practical problems. Each project is modular, demo-ready, and designed for recruiter-friendly review.

---

## 📦 Projects in This Suite

### 1. ✈️ [Flight Club](./flight_club/README.md)
A flight deal scanner that uses the Amadeus API and Google Sheets to monitor destination prices and send email alerts when prices drop.

### 2. 📊 [Habit Tracker](./habit_tracker/README.md)
Tracks productivity or fitness minutes with the Pixela API. Visualizes progress in real-time graphs and supports logging/editing from a clean CLI.

### 3. 🏋️ [Workout Tracker](./workout_tracker/README.md)
Parses natural-language workout input using the Nutritionix API and logs structured workout data (duration, calories) into Google Sheets.

---

## 🧰 Tech Stack

- **Python**  
- **APIs:** Amadeus, Pixela, Nutritionix, Sheety  
- **Google Sheets** as a lightweight backend (via Sheety)  
- **dotenv** for secure credential management  
- **Requests** for API integration  
- **CLI design** with flexible, testable menus  
- **Demo modes** built into each tool for easy testing

---

## 💡 What I Learned

- Structuring multiple real-world CLI tools in a single portfolio  
- Managing API authentication and error handling professionally  
- Building modular, readable, and scalable automation scripts  
- Making tools demo-friendly for recruiters without setup

---

## 📂 Project Structure

```
spreadsheet-tools-suite/
├── flight_club/
├── habit_tracker/
├── workout_tracker/
├── .gitignore
└── README.md
```

Each subfolder contains its own codebase, README, `.env.example`, and dependencies.

---

## 🔧 How to Run Any Tool

1. Clone the repo:

```bash
git clone https://github.com/yourusername/spreadsheet-tools-suite.git
cd spreadsheet-tools-suite/<tool_name>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add a `.env` file based on `.env.example`  
   Or enable demo mode in `main.py` if available

4. Run the tool:

```bash
python main.py
```

---

## 🌟 Why This Project Matters

This suite showcases:
- ✅ Hands-on experience with APIs  
- ✅ Secure practices with environment management  
- ✅ Real automation — not just tutorials  
- ✅ Clean CLI workflows, built to be extended

It reflects the ability to build, organize, and present real-world Python tools for both users and hiring managers.
