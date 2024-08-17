# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once).

numbers = set()

for i in range(8):
    numbers.add(int(input("Enter number: ")))

print(numbers)


