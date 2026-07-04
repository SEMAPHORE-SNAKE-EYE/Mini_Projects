import random
import hangman_art
import hangman_words


print(hangman_art.logo)
lives = 6

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"You Are left with : {lives} lives ")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"you entered a letter they've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess) # This is to add letter in correct_letters, to save it .

        elif letter in correct_letters:
            display += letter #It is what allows previously guessed correct letters to remain visible.

        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"Your Gussed {guess}.Its a Wrong word ")

        if lives == 0:
            game_over = True
            print(f"YOU LOST. The Correct word is  : {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****** YOU WON ******")
    print(hangman_art.stages[lives])
