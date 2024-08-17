# 5. Write a program which finds out whether a given name is present in a list or not.

myList = ["Ram", "Shyam", "Hari", "Sita", "Gita"]

name = input("Enter Your Name: ")

if(name or name.capitalize in myList):
    print("Name is present in the list.")
else:
    print("Name is not present in the list.")

