import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(c_direction, c_text, c_shift):
    cipher = ""
    index = 0
    for letter in c_text:
        index = alphabet.index(letter)
        if c_direction == "decode":
            math.fabs(c_shift)
            c_shift *= -1
        cipher += alphabet[index + c_shift]
    print(f"The {c_direction}d text is {cipher}")

ceasar(c_direction=direction, c_text=text, c_shift=shift)