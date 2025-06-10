# 🧠📋 Python Mini Projects

This repository contains two beginner-friendly yet practical Python applications:

1. **To-Do List Manager** (`Todo_listApp.py`)
2. **Quiz Application** (`QuizApp.py`)

Each project demonstrates how to work with file handling, user input, and basic control flow in Python.

---

## 📝 1. To-Do List Manager

A simple terminal-based task manager that lets users:
- Add tasks
- View existing tasks
- Delete tasks

### 🔧 Features
- Reads and writes tasks from a `.txt` file.
- Allows filename customization via user input.
- Handles invalid inputs and missing files.

### 📂 Files
- `Todo_listApp.py` – Main Python script.
- `TodoList.txt` – Sample task file (can be customized or replaced).

### ▶️ How to Run
```bash
python Todo_listApp.py
```

### 🖥️ Sample Usage
```
Enter file name: TodoList
Choose an action:
1. Add task
2. View tasks
3. Delete task
4. Exit
Enter your choice (1-4): 2

Tasks in TodoList.txt:
1. Buy groceries
2. Complete math homework
...
```

---

## 🎯 2. Quiz Application

A simple command-line quiz app that:
- Loads multiple-choice questions from a JSON file.
- Compares answers in a case-insensitive way.
- Displays the final score after completion.

### 📂 Files
- `QuizApp.py` – Main quiz script.
- `ques.json` – Question bank in JSON format.

### ▶️ How to Run
```bash
python QuizApp.py
```

### 🧪 Sample Interaction
```
Q1. Capital of France? paris
Q2. Largest planet in our solar system? jupiter
...

Your score: 28/30
```

### ✅ JSON Format
```json
[
  {"q": "Capital of France?", "a": "Paris"},
  {"q": "Largest planet in our solar system?", "a": "Jupiter"}
]
```

---

## 🛠️ Requirements
- Python 3.x
- No external libraries needed

---

## 📌 Notes
- Ensure the question file `ques.json` and the to-do file `TodoList.txt` are in the same directory when running the respective scripts.
- Both apps are built for CLI (Command-Line Interface) environments.

---

## 🤝 Contribution
Feel free to fork the repo, add your own features (like due dates or timed quizzes), and make pull requests.

---

## 📃 License
This project is licensed under the MIT License.

---
