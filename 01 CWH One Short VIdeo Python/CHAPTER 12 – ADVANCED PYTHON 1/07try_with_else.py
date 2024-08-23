try:
    a = int(input("Enter a number: "))
    print("a =", a)

except Exception as e:
    print( e)
    
else:
    print("a is a number")