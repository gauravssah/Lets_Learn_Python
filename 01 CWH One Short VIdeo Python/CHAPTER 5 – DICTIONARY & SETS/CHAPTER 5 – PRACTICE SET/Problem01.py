# 1. Write a program to create a dictionary of Hindi words with values as their English

dictonary = {
    "pankha" : "Fan",   
    "ghar" : "House",
    "guitar" : "Instrument",
    "laptop" : "Computer",
    "phone" : "Mobile",
    "book" : "Book",
}

print(dictonary) # {'pankha': 'Fan', 'ghar': 'House', 'guitar': 'Instrument'}
print(dictonary["pankha"]) # Fan
print(dictonary.get("pankha")) # Fan


# -------------------------
# Taking From User Input

word = input("Enter word: ")
print(dictonary[word])











