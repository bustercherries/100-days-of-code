rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
computer_choice = int(random.randint(0,2))

# rock = 0
# paper = 1
# scissors = 2

if choice == 0:
    print(rock)
    if computer_choice == 0:
        print("Copmuter chose:\n" + rock)
        print("It's a tie, try again")
    elif computer_choice == 1:
        print("Computer chose:\n" + paper)
        print("You lose")
    elif computer_choice == 2:
        print("Computer chose:\n" + scissors)
        print("You win.")
elif choice == 1:
    print(paper)
    if computer_choice == 0:
        print("Computer chose:\n" + rock)
        print("You win.")
    elif computer_choice == 1:
        print("Computer chose:\n" + paper)
        print("Its' a tie.")
    elif computer_choice == 2:
        print("Computer chose:\n" + scissors)
        print("You lose.")
elif choice == 2:
    print(scissors)
    if computer_choice == 0:
        print("Computer chose:\n" + rock)
        print("You lose.")
    elif computer_choice == 1:
        print("Computer chose:\n" + paper)
        print("You win.")
    elif computer_choice == 2:
        print("Computer chose:\n" + scissors)
        print("It's a tie.")
