# 6. Write a python function which converts inches to cms.

inc = int(input("Enter the inches: "))

def incToCm(inc):
    return inc*2.54

print(f"{inc} inches is {incToCm(inc)} cms")

