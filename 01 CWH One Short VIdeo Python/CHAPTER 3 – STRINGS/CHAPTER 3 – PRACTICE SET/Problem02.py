# 2. Write a program to fill in a letter template given below with name and date.

"""
letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|
"""
# ------------------------------

name = input("Enter your name: ")
date = input("Enter date: ")

letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))

# ------------------------------

print("Printing using f-string")
print(f"Dear {name},\nYou are selected!\n{date}")

# ------------------------------

newletter = f"""
Dear {name},
You are selected!
{date}
"""

print("Printing using new letter")
print(newletter)
