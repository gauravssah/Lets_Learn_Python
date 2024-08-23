def mai():
    try:
        a = int(input("Enter a number: "))
        print("a =", a)
        return

    except Exception as e:
        print( e)
        return

    finally: # will always execute even if there is an exception or not.
        print("I am always executed")
        

mai()