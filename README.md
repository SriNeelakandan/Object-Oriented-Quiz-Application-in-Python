# 🧠 Python Quiz App (OOP-Based)

This is a simple **command-line Quiz Application** built using Python and Object-Oriented Programming (OOP).
It fetches questions from a data source and quizzes the user interactively, showing the final score at the end.

## 📋 Project Description

- The app reads multiple-choice questions and answers from a **Python dictionary list** (`question_data`).
- Each question is modeled using a **`Question` class**.
- The quiz logic (handling current question, checking answers, updating scores) is managed by the **`QuizBrain` class**.
- The quiz continues until there are no more questions left.
- At the end, the final score is displayed.

## 🧱 Project Structure

quiz_app/
│
├── main.py # Main script that runs the quiz
├── question_model.py # Defines the Question class
├── quiz_brain.py # Quiz logic class (QuizBrain)
├── data.py # Contains the question_data list
└── README.md # Project documentation

## 🛠️ Tools & Technologies

- Python 3.x
- Object-Oriented Programming (OOP)
