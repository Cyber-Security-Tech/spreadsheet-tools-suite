# 🧠 Habit Tracker – Spreadsheet Tools Suite

A real-world Python tool that helps you build better habits by logging daily progress (like coding minutes, workouts, reading, etc.) to beautiful visual graphs using the Pixela API. It includes advanced features like graph switching, undo, custom date entry, and real-time tracking feedback — all integrated into a clean CLI experience.

🧩 This is one of three tools in the **Spreadsheet Tools Suite**, a collection of real-world Python automation projects using Google Sheets or visual dashboards to track personal productivity.

## 🚀 Interactive CLI Included

Track your habits in seconds with a polished command-line interface:

```bash
python main.py
```

```text
📊 Habit Tracker Menu
1. Log today's habit
2. Log habit for a custom date
3. Undo today's entry
4. Open graph in browser
5. Exit
6. View today's logged minutes
```

You can select between different graphs (e.g., "Productivity" or "Workout"), and each graph logs to its own Pixela visual tracker.

---

## 🔧 Features

- ✅ Real-time habit logging via Pixela API
- ✅ Track multiple graphs (e.g. productivity, fitness)
- ✅ Flexible date input (YYYYMMDD, YYYY-MM-DD, or YYYY/MM/DD)
- ✅ Undo/delete today's entry with one click
- ✅ View your current log total for today
- ✅ Automatically open your graph in browser
- ✅ Clean, interactive CLI menu
- ✅ Secure `.env` usage with `.env.example` provided

---

## 📂 Project Structure

```
habit_tracker/
│
├── main.py              # Interactive CLI menu for the Habit Tracker
├── habit_api.py         # All Pixela API functions (log, get, delete, open)
├── config.py            # Loads credentials from .env
├── .env.example         # Template for environment variables
├── .gitignore           # Ignore compiled files and .env
└── README.md            # Project documentation
```

---

## 🔒 Environment Variables

Create a `.env` file inside `habit_tracker/` with the following:

```
PIXELA_USERNAME=your_pixela_username
PIXELA_TOKEN=your_secure_token
PIXELA_GRAPH_ID=tracker1
```

> Use `.env.example` as a reference template.

---

## 📊 Visual Graphs

Each habit you log is visualized as a clean dot-style graph via Pixela. You can open the graph from the CLI or manually at:

```
https://pixe.la/v1/users/your_username/graphs/your_graph_id.html
```

---

## 🧪 How to Run

1. Clone the repo
2. Create a Pixela account (run `main.py` to do it automatically or manually via API)
3. Add your `.env` file
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the app:

```bash
python main.py
```

---

## 💡 What I Learned

- Working with REST APIs (Pixela) to post, delete, and fetch data
- Handling flexible user input formats
- Building professional interactive CLI tools
- Tracking habits visually with real-world automation

---

## 👀 Why This Project Matters

This tool demonstrates:

- ✅ Real-world API integration
- ✅ Automation for daily routines
- ✅ CLI design skills
- ✅ Visual productivity tracking

It blends software engineering and habit science into a clean, minimalist Python project.

---

## 🤝 Let's Connect

If you're a recruiter or hiring manager interested in practical Python automation and CLI tools, feel free to connect with me! I'd love to bring these skills to your team.
