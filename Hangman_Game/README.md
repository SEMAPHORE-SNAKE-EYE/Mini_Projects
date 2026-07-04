# 🎮 Hangman Game (Python)

A simple command-line Hangman game built using Python. The player has to guess the hidden word one letter at a time before running out of lives.

---

## 📌 Features

- Guess one letter at a time
- Tracks correct and incorrect guesses
- Prevents duplicate guesses
- Displays remaining lives
- Win and lose conditions
- ASCII Hangman stages (if included)

---

## 🛠️ Technologies Used

- Python 3

---

## 📂 Project Structure

```
hangman/
│── main.py
│── hangman_words.py
│── hangman_art.py
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/hangman-game.git
```

2. Navigate to the project folder

```bash
cd hangman-game
```

3. Run the game

```bash
python main.py
```

---

## 🎮 How to Play

- A random word is selected.
- Guess one letter at a time.
- If the letter exists in the word, it is revealed.
- If the guess is incorrect, you lose one life.
- Continue guessing until:
  - You reveal the complete word (Win 🎉)
  - You run out of lives (Lose 💀)

---

## 📸 Sample Output

```
You have 6 lives.

Guess a letter: a

_ a _ _ _

You have 6 lives.

Guess a letter: p

a p p _ _

Congratulations! You guessed the word.
```

---

## 📚 Concepts Used

- Variables
- Loops
- Conditional Statements
- Lists
- Strings
- Random Module
- Functions
- User Input

---

## 🚀 Future Improvements

- Difficulty Levels
- Scoreboard
- Timer
- Categories (Animals, Movies, Countries)
- GUI using Tkinter or Pygame

---

## 👨‍💻 Author

**Kartik Badkhal**

GitHub: https://github.com/kabadkhal
LinkedIn: https://www.linkedin.com/in/kabadkhal/
