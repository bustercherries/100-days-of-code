import os
from art import bid_logo
# os.system('cls||clear')

print(bid_logo)
dictionary = {}
flag = True

def highest_bidder(bidding_record):
    highest_amount = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if int(bid_amount) > highest_amount:
            highest_amount == int(bid_amount)
            winner = bidder
    print(f"The winner is {winner} with the amount ${highest_amount}.")

while flag:
    name = input("What is your name?\n")
    bid_price = input("What is your bid price?\n")
    
    dictionary[name] = bid_price

    answer = input("Are there other users who wants to bid? Type 'yes' or 'no'.\n")

    if answer == "yes":
        os.system('cls||clear')
        flag = True
    elif answer == "no":
        highest_bidder(dictionary)
        flag = False
