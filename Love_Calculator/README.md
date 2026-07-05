# ❤️ Love Score Calculator (Python)

A simple Python project that calculates a **Love Score** between two names by counting the occurrences of the letters in the words **TRUE** and **LOVE**.

## 📌 How It Works

1. Combines both names into a single string.
2. Converts the string to lowercase.
3. Counts the occurrences of the letters:

   * **TRUE** → `T`, `R`, `U`, `E`
   * **LOVE** → `L`, `O`, `V`, `E`
4. Adds the counts for each word.
5. Combines the two totals to generate the final Love Score.

### Example

**Input**

```python
calculate_love_score("Kanye West", "Kim Kardashian")
```

**Output**

```text
42
```

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
love-score-calculator/
│── main.py
└── README.md
```

---

## 💻 Sample Code

```python
def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).lower()

    true_score = (
        combined_name.count("t") +
        combined_name.count("r") +
        combined_name.count("u") +
        combined_name.count("e")
    )

    love_score = (
        combined_name.count("l") +
        combined_name.count("o") +
        combined_name.count("v") +
        combined_name.count("e")
    )

    print(f"{true_score}{love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")
```

---

## 🎯 Learning Objectives

* Python Functions
* String Manipulation
* String Methods (`lower()`, `count()`)
* Variables
* f-Strings
* Basic Problem Solving

---

## 📜 License

This project is created for learning and practice purposes.
