# guss the number

import random

randNum = random.randint(0, 10)  # generates a random integer between 0 and 10
print(randNum)

class Game:                                                          
    def guess(self, num):
       if num == randNum:
           print("You guessed right")
       elif num > randNum:
           print("Too high")
       else:
           print("Too low")

n = int(input("Guess the number : "))

user = Game()
user.guess(n)
