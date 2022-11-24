import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
game_over = False
lives = 6

print(hangman_art.logo)
print(chosen_word)

display = []

for letter in range(len(chosen_word)):
    display.append("_")

while game_over == False:

    guess_letter = input("Guess a letter: ")

    if guess_letter in display:
        print(f"Dude, you have already guessed this letter: {guess_letter}")

    if guess_letter in chosen_word:
        print("You guessed a letter correctly.")

        for position in range(len(chosen_word)):
            chosen_letter = chosen_word[position]
            if chosen_letter == guess_letter:
                display[position] = guess_letter

    elif guess_letter not in chosen_letter:
        lives -= 1
        print("Dude, you have chosen the wrong letter!")
    
    if lives == 0:
        game_over = True
        print("Sorry to inform you but you lost it. \nThis is the end of this game.")

    if not "_" in display:
        game_over = True

    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])
