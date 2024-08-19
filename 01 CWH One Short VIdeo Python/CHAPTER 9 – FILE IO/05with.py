"""
f = open("file.txt")
print(f.read())
f.close()

"""

# This can be done using with, and you don't need to close the file
with open("file.txt") as f:
    print(f.read())

