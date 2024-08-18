# 7. Write a python function to remove a given word from a list ad strip it at the same 
# time.

l = ["Hello", "World", "Python"]

print(l)

w = input("Enter the word to be removed: ")

def removeWord(l, w):
    n = []
    for item in l:
        if item != w:
            n.append(item.strip(w))
    return n

print(removeWord(l, w))



