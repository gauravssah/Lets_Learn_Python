# 2. Write a class “Calculator” capable of finding square, cube and square root of a 
# number.

class Calculator:
    def __init__(self, n):
        self.num =n
    
    def square(self):
        return self.num*self.num
    
    def cube(self):
        return self.num*self.num*self.num
    
    def squareRoot(self):
        return self.num**0.5


obj = Calculator(25)
print("Square: ",obj.square())
print("Cube: ",obj.cube())
print("Square Root: ",obj.squareRoot())

