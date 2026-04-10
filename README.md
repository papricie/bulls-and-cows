# Bulls and Cows

A simple number guessing game built in Python.  
The project focuses on clean code structure, testability, and basic QA practices.

---

## About the project

Bulls and Cows is a classic logic game where the player tries to guess a secret 4-digit number.

Each digit is unique and the number does not start with 0.

After each guess, the player receives feedback:

- **Bull** → correct digit in the correct position  
- **Cow** → correct digit in the wrong position  

---

## Rules

- The secret number has 4 digits
- All digits are unique
- The number cannot start with 0
- The player must guess the number
- The game ends when the player gets 4 bulls

---

## Tech stack

- Python 3
- Pytest (unit testing)
- CLI interface

---

## Project structure
```
bulls-and-cows/
│
├── src/
│ └── bulls_and_cows/
│ │── __init__.py
│ ├── generator.py
│ ├── evaluator.py
│ ├── validator.py
│ └── game.py
│
├── tests/
│ └── test_evaluator.py
│
├── cli.py
├── requirements.txt
└── README.md
```


---

## How to run the project

Make sure you are in the project root directory.

```bash
python -m venv venv
```
```bash
venv\Scripts\Activate.ps1
```
```bash
pip install 
```
```bash
python cli.py
```

## How to run tests

Run all unit tests using:

```bash
python -m pytest -v
```

## Example gameplay
- Welcome to Bulls and Cows!

- Try to guess a 4-digit number.

- Enter your guess: 1234
- Result: 1 bull, 2 cows

- Enter your guess: 5678
- Result: 0 bulls, 0 cows

## What I learned in this project
- How to structure a Python project using src/ layout
- Writing unit tests with pytest
- Separating logic from input/output (clean architecture basics)
- Debugging real bugs (edge cases with duplicates)
- Working with Git and incremental commits

## Possible future improvements
- Web version (Flask / Streamlit)
- Difficulty levels
- Attempt counter / scoring system
- Better UI/UX for CLI
- CI pipeline with GitHub Actions

## Author

Patricie Hermanová

Python beginner building projects for QA / junior developer role