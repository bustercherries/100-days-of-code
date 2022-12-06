import math
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceasar(c_direction, c_text, c_shift):
    cipher = ""
    x = 0
    if c_direction == "decode":
            c_shift *= -1
    for char in c_text:
        if char in alphabet:
            x = alphabet.index(char)
            cipher += alphabet[x + c_shift]
        else:
            cipher += char
    print(f"The {c_direction}d text is {cipher}")

print(art.logo)
 
should_countine = True
while should_countine:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(c_direction=direction, c_text=text, c_shift=shift)

    shift %= len(alphabet) 
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if answer == 'no':
        should_countine = False
        print("Goodbye!")


