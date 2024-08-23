a = 100

def myfun():
    global a
    a = 10
    print(a)
    
print(a)
myfun()