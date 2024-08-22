a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if b == 0:
    raise ZeroDivisionError("Here b can't be zero")
else:
    print(f"a / b = {a/b}")



print("Bye")
