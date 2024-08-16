# 3. Write a program to detect double space in a string.
# 4. Replace the double space from problem 3 with single spaces.


word = input("Enter a word: ")

if "  " in word:
    print("There is a double space")
    print(word.find("  "))
    print(word.replace("  ", " "))
else:
    print("There is no double space")






