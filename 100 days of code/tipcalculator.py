print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
no_people = input("How many people to split the bill? ")

x = ((float(bill) * float(tip)/100) + float(bill))/ int(no_people)
final_amount = "{:.2f}".format(x)
print(f'Each person should pay: ${final_amount}')