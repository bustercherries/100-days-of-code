def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

dictionary = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

num1 = int(input("What's the first number?\n"))

for symbol in dictionary:
    print(symbol)

operation_symbol = input("Pick a symbol from the above: ")
num2 = int(input("What's the second number?\n"))

function = dictionary[operation_symbol]
first_answer = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another symbol: ")
num3 = int(input("What's the next number?\n"))
function = dictionary[operation_symbol]
second_answer = function(function(num1, num2), num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")