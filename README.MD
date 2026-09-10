# Trivia Quiz Game

A terminal-based trivia quiz game inspired by "Kaun Banega Crorepati" (KBC), built with Python and MySQL. Players answer multiple-choice questions across 8 increasing difficulty levels, with prize money doubling at each stage. Get one wrong, and the game ends — clear all 8, and you win the jackpot.

## Features

- 8 difficulty levels (₹1,000 to ₹1,00,00,000), covering sports, pop culture, history, general knowledge, geopolitics, science & tech, and current affairs
- Player login/registration system
- Persistent stats tracking (games played, questions answered correctly, best score)
- Top 5 leaderboard

## Tech Stack

- Python 3
- MySQL

## Setup Instructions

### 1. Install MySQL Server
If you don't already have it, download and install from:
https://dev.mysql.com/downloads/installer/

During setup, you'll be asked to set a **root password** — remember it, you'll need it in step 5.

### 2. Clone this repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up the database
Run these two commands from the project folder (you'll be prompted for your MySQL root password):
```bash
mysql -u root -p < schema.sql
mysql -u root -p trivia < question_bank.sql
```

This creates the `trivia` database, all required tables, and loads 64 trivia questions across 8 levels.

### 5. Add your MySQL password
Open `main.py` and replace `"your_password"` with your actual MySQL root password:
```python
connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",   # <-- change this
    database="trivia"
)
```

### 6. Run the game
```bash
python main.py
```

## How to Play

1. Enter your name to log in (or register, if it's your first time)
2. Answer each question by typing `a`, `b`, `c`, or `d`
3. Get it right → move to the next level and a bigger prize
4. Get it wrong → game over, you keep your current winnings
5. Check the leaderboard anytime from the main menu to see the top 5 players

## Project Structure

```
├── main.py            # Game logic and entry point
├── schema.sql          # Database table definitions
├── question_bank.sql   # 64 trivia questions across 8 levels
├── requirements.txt    # Python dependencies
└── .gitignore
```