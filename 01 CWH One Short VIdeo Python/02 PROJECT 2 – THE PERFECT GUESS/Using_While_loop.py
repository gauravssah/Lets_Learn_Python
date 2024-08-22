import random

n = random.randint(1, 10)
a = -1

gussessTime = 0

while(a != n):
    a = int(input("Guess the number : "))
    gussessTime += 1
    if(a == n):
        print("You guessed right")
    elif(a < n):
        print("Too low")
    else:
        print("Too high")

print("You took " + str(gussessTime) + " gussess")





