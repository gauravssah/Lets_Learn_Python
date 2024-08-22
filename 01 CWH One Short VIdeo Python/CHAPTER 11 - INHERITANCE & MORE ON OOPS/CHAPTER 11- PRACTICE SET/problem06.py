# 6. Write __str__() method to print the vector as follows:

#    7i + 8j +10k 

class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0][0] 
            self.y = args[0][1]
            self.k = args[0][2]
        else:
            self.x = args[0]
            self.y = args[1]
            self.k = args[2]

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.k}k" 
    

v1 = Vector(7, 8, 10)
print(v1)




