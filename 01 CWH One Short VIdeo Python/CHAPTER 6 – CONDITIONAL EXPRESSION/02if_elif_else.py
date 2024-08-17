age = int(input("Enter Your Age: "))

# This is if-elif-else statement

if(age >= 18):
    print("You Can Vote")
elif(age <0):
    print("Invalid Age!")
elif(age == 0):
    print("You Enter Zero")
else:
    print("You Can't Vote")

print("Thank You")

