# 4. Write a program to find whether a given username contains less than 10 
# characters or not.


username = input("Enter Your Username: ")

if(len(username) < 10):
    print("Your Username contains less than 10 characters.")
else:
    print("Your Username contains more than 10 characters.")

