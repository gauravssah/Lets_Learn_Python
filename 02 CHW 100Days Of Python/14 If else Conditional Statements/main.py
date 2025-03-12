# age = int(input("Enter Your Age: "))
age = input("Enter Your Age: ")
name = input("Enter Your Name: ")


if int(age)<18:
    print("You can't drive, you need to wait atlist: ", 18-int(age), "Years")  
else:
    print("You can drive", name)

