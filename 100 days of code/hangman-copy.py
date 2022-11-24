import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)
print(chosen_word)

display = []

for letter in range(len(chosen_word)):
    display.append("_")


guess_letter = input("Guess a letter: ")

if guess_letter in chosen_word:
    print("You guessed a letter correctly.")

    for position in range(len(chosen_word)):
        chosen_letter = chosen_word[position]
        print(f"chosen letter to:{type(chosen_letter)}")
        if chosen_letter == guess_letter:
            display[position] = guess_letter


    print(display)
