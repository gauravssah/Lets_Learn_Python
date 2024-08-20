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
        return self.num


obj = Calculator(5)
print(obj.square())
print(obj.cube())
print(obj.squareRoot())

