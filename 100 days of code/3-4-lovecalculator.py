# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_string = name1.lower() + name2.lower()

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")

count_numbers1 = t + r + u + e

l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e")

count_numbers2 = l + o + v + e

score = int(str(count_numbers1) + str(count_numbers2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")