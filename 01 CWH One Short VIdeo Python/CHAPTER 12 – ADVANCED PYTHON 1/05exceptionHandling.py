try:
    a = int(input("Enter a number: "))
    print("a =", a)
    
except ValueError:
    print("a is not a number")

except Exception as e:
    print( e)


print("Bye")


