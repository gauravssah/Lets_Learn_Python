# 2. Write a python program using function to convert Celsius to Fahrenheit.

def CtoF(c):
    return (c*9/5) + 32


c = int(input("Enter the temperature in Celsius: "))
print(f"{c}C is {CtoF(c)}F")
