class Numbers:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    
    def __add__(self, other):
        return self.a + other.a 

    def __sub__(self, other):   
        return self.a - other.a, self.b - other.b   

    def __mul__(self, other):
        return self.a * other.a, self.b * other.b
    

    def __truediv__(self, other):
        return self.a / other.a, self.b / other.b
    

    def __floordiv__(self, other):
        return self.a // other.a, self.b // other.b


    def __mod__(self, other):
        return self.a % other.a, self.b % other.b


    def __pow__(self, other):
        return self.a ** other.a, self.b ** other.b 
    

a = Numbers(2, 3)
b = Numbers(4, 5)

print(a + b)    #  6
print(a - b)    # (-2, -2)
print(a * b)    # (8, 15)
print(a / b)    # (0.5, 0.6)
print(a // b)   # (0, 0)
print(a % b)    # (2, 3)
print(a ** b)   # (16, 243)  







