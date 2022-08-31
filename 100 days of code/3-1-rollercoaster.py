print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets is 5$")
    elif age <= 18:
        bill = 7
        print("Youth ticket is 7$")
    else:
        bill = 12
        print("Adult ticket is 12$")

    answer = input("Do you want to have a photo? Y or N? ")
    if answer == "Y":
        bill += 3
    print(f"Your final bill costs {bill}$")

else:
    print("Sorry, you have to grow taller before you can ride.")
