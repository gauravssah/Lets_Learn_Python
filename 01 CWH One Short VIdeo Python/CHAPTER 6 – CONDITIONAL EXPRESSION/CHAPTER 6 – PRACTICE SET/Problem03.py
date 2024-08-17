# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

comment = input("Enter Your Comment: ")

if("Make a lot of money" in comment):
    print("This is Spam.")
elif("buy now" in comment):
    print("This is Spam.")
elif("subscribe this" in comment):
    print("This is Spam.")
elif("click this" in comment):
    print("This is Spam.")
else:
    print("Not Spam.")

