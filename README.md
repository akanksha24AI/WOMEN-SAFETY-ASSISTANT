# Women Safety Assistant

A simple Python terminal-based safety assistant designed to provide useful safety information and basic emergency guidance in one place. The project is created as a beginner-friendly Python application that can be run directly from the terminal.

## Features

* Provides **Safety Tips** for everyday situations
* Displays important **Emergency Numbers** such as 112, 100, 181, 1091, 108, and 1098
* Provides an **SOS Help** option with basic emergency guidance
* Allows users to save a **temporary emergency contact** during the current session
* Simple **menu-based terminal interface**
* Handles invalid menu choices
* Uses basic Python concepts and requires no external libraries

## Technology Stack

* **Python 3**
* Python `print()` and `input()`
* Functions
* Conditional statements
* Loops
* Lists
* Terminal / Command Line

## Project Structure

```text
Women-Safety-Assistant/
│
├── women_safety.py
└── README.md
```

## How to Run

### 1. Make sure Python is installed

Check the installed Python version:

```bash
python --version
```

### 2. Open the project folder

Open the project folder in VS Code and start the terminal.

### 3. Run the program

```bash
python women_safety.py
```

The Women Safety Assistant menu will appear in the terminal.

## Menu Options

```text
1. Safety Tips
2. Emergency Numbers
3. SOS Help
4. Emergency Contact
5. Exit
```

Select the required option by entering its number.

## Emergency Numbers

The application provides commonly used emergency numbers:

| Service           | Number |
| ----------------- | -----: |
| Emergency         |    112 |
| Police            |    100 |
| Women Helpline    |    181 |
| Women in Distress |   1091 |
| Ambulance         |    108 |
| Child Helpline    |   1098 |

## SOS Help

The SOS section provides basic guidance for an emergency situation.

It is an **educational feature only**. The program does not actually place emergency calls, send messages, or share the user's location.

For a real emergency, the user should contact the appropriate emergency service directly.

## Emergency Contact

The Emergency Contact option allows the user to enter a trusted person's name and phone number.

The information is used only during the current program session and is not stored permanently.

## Concepts Used

This project demonstrates basic Python programming concepts such as:

* Functions
* Variables
* User input
* `if-elif-else` statements
* `while` loops
* Lists
* String handling
* Menu-driven programming

## Future Improvements

Possible improvements for future versions include:

* Real SOS alert functionality
* Location sharing
* Permanent emergency contact storage
* Graphical user interface
* More detailed emergency guidance
* Additional safety resources

