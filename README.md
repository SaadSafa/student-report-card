# Student Report Card Management System

This is a simple Python console application to manage student data, courses, grades, and generate reports. It supports adding students, courses, calculating averages, ranking students, and saving/loading data from JSON files.

## Features

- Add new students with name and year
- Add courses and grades to students
- View detailed student reports
- Display all students
- Delete a student by ID
- Rank students by average grade
- Save and load data to/from JSON files
- Command-line menu-driven interface

## Requirements

- Python 3.x

## How to Run

1. Clone the repository
2. Open terminal in project folder
3. Run the main program:

```bash
python main.py


## 🧪 Run Tests

To run the unit tests locally:

```bash
python -m unittest discover


## 📂 Project Structure

StudentReportCard/
│
├── StudentReportCardMngSys.py   # Core logic (Student, School classes)
├── test_school.py               # Unit tests for Student and School
├── main.py                      # Entry point of the application
├── README.md                    # Project documentation
├── .gitignore                   # Git ignored files
└── __pycache__/                 # Python bytecode (auto-generated)

