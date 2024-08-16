# 3. Check the type of variable assigned using input () function.

# This program is used to check the type of variable assigned using input () function.
# Input () function is used to take input from user.
# Output : The type of variable assigned using input () function is <class 'str'> || Its a default output.



a = input("Enter the value: ")
print("The type of variable assigned using input () function is ",type(a)) # <class 'str'>


b = int(input("Enter the value: "))
print("The type of variable assigned using input () function is ",type(b)) # <class 'int'>


c = float(input("Enter the value: "))
print("The type of variable assigned using input () function is ",type(c)) # <class 'float'>

s = str(input("Enter the value: "))
print("The type of variable assigned using input () function is ",type(s)) # <class 'str'>


