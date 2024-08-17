# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if "S" in name:
        print(f"Hello {name}")
    else:
        print(name)
else:
    print("All Done")



