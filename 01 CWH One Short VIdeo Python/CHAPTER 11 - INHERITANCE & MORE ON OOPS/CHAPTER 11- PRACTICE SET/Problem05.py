# 5. Write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them.


class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0][0] 
            self.y = args[0][1]
        else:
            self.x = args[0]
            self.y = args[1]    

    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y))

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
v4 = v1 * v2
print(v3)
print(v4)
















