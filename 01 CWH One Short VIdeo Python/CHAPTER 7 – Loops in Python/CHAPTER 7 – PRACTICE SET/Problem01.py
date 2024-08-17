# 1. Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter a number: "))

i = 1

print("Printing using while loop")
while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1

print("Printing using for loop")

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")





