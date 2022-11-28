import math

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5

def calculator(height = test_h, width = test_w, cov = coverage):
    number_of_cans = (height*width)/cov
    print(f"The number of cans: {math.ceil(number_of_cans)}")

calculator()