# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

name = input("Enter Your Name: ")

sub1 = int(input("Enter Marks of Subject 1: "))
sub2 = int(input("Enter Marks of Subject 2: "))
sub3 = int(input("Enter Marks of Subject 3: "))

total = sub1 + sub2 + sub3
avg = total / 3

if(avg >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print(f"Congratulations!\n\t{name} \nYou have passed the exam.")
else:
    print(f"Sorry! \n\t{name} You have failed the exam.")
