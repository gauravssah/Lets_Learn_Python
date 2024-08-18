"""
1. We all have played snake, water gun game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user.
 
snake = 1
water = -1
gun = 0

"""

# ---------------------------------------

import random

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

while True:
    
    computer = random.choice([-1,0, 1])
    youStr = input("Enter 's' for snake, 'w' for water, 'g' for gun: ")
    you = youDict[youStr]

    print(f"You choose : {reverseDict[you]}\nComputer choose : {reverseDict[computer]}")

    if you == computer:
        print("Tie")
    elif you == 1 and computer == 0:
        print("You win")
    elif you == 0 and computer == 1:
        print("Computer win")
    elif you == -1 and computer == 0:
        print("Computer win")
    elif you == 0 and computer == -1:
        print("You win")
    elif you == 1 and computer == -1:
        print("You win")
    elif you == -1 and computer == 1:
        print("Computer win")
    
    print("----------------------------")

    ch = input("Do you want to continue? (y/n): ")
    if ch == "n":
        print("Thanks for playing")
        break
    else:
        computer = random.choice([-1,0, 1])
    
    
    





