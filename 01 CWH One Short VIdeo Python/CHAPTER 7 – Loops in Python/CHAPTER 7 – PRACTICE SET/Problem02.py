# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S.

l = ["Harry", "Soham", "Sachin", "Rahul", "ROSHAN", "Rishabh"]

for name in l:
    if (name.startswith("S")):
        print(f"Hello {name}")
    else:
        print(name)
else:
    print("All Done")

# Output -
#       Harry
#       Hello Soham
#       Hello Sachin
#       Rahul
#       ROSHAN
#       Rishabh
#       All Done

