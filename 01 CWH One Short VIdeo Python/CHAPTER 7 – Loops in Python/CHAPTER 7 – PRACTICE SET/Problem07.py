# 7. Write a program to print the following star pattern.

"""
Like :- for n = 3

      *
     ***
    ***** 

"""


n = int(input("Enter the number : "))

for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1)) 
   

