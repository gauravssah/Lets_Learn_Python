# 1. Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.

class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f"The vector is: {self.x}i + {self.y}j")
    

class ThreeDVector(TwoDVector):
    def __init__(self, x, y,k):
        self.k = k
        super().__init__(x, y)  
        
    def show(self):
        print(f"The vector is: {self.x}i + {self.y}j + {self.k}k")
    

v1 = TwoDVector(1, 2)
v1.show()

v2 = ThreeDVector(1, 3,5)
v2.show()



