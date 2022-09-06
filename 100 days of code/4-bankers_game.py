import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_of_people = len(names)
print(number_of_people)
index = random.randint(0,number_of_people)
winner = names[index]
print(winner +" is going to pay a bill!")

