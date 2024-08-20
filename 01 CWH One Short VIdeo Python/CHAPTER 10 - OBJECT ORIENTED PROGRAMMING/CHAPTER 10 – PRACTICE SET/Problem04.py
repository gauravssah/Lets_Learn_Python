# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, n):
        self.num =n
    
    def square(self):
        return self.num*self.num
    
    def cube(self):
        return self.num*self.num*self.num
    
    def squareRoot(self):
        return self.num

    @staticmethod
    def greet():
        print("Hello")  

obj = Calculator(5) 
obj.greet() 




