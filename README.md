# The Fall of the Tyrant

## Overview

**The Fall of the Tyrant** is a decision-based text adventure game developed in Python.  
The player assumes the role of a mercenary seeking revenge against a ruthless feudal lord known as *The Tyrant*.  

The outcome of the story is determined by the player's decisions, which directly influence character attributes and the final confrontation.

---

## Objectives of the Project

This project was developed as a practical exercise to strengthen fundamental programming skills in Python, including:

- Writing and organizing functions
- Managing program flow
- Handling user input
- Implementing conditional logic
- Passing and returning values between functions
- Maintaining and modifying game state variables

---

## Game Mechanics

The game includes:

- Multiple narrative branches
- Several possible endings
- A basic RPG-style system featuring:
  - Health tracking
  - Reputation tracking
- Dynamic narrative using formatted strings (f-strings)
- Structured architecture centered around a `main()` control function

Player statistics are updated based on decisions and influence the outcome of the final battle.

---

## Technical Structure

The program is organized into modular functions:

- `intro()` – Introduces the narrative and initiates the game
- `choose_weapon()` – Handles initial player setup
- `sword_path()` – Manages sword-based decisions
- `bow_path()` – Manages bow-based decisions
- `final_battle()` – Determines the ending based on player stats
- `main()` – Controls overall program execution

This structure improves readability, maintainability, and scalability.

---

## Requirements

- Python 3.x

---

## How to Run

1. Download the project file.
2. Open a terminal in the project directory.
3. Run:

