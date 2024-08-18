# 1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

print(f"The greatest number in {n1}, {n2}, {n3} is : {greatest(n1,n2,n3)}")

