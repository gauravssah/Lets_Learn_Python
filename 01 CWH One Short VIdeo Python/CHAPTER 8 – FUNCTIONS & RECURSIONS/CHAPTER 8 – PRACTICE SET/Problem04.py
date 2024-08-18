# 4. Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter the number: "))

def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

print(f"The sum of first {n} natural numbers is : {sum(n)}")




