
test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5

def calculator(height = test_h, width = test_w, cov = coverage):
    number_of_cans = round((height*width)/cov)
    print(number_of_cans)

calculator()