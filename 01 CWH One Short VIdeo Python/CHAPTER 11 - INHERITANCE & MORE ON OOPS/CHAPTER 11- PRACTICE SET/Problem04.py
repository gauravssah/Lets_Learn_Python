# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.
   
class Complex: 

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __mul__(self, other):
        return Complex((self.real * other.real) - (self.imaginary * other.imaginary), (self.imaginary * other.real) + (self.real * other.imaginary))
        
    
    def __str__(self):
        return str(self.real) + " + " + str(self.imaginary) + "i"
    
    def Display(self):
        print(self.real, "+", self.imaginary, "i")

c1 = Complex(2, 3)
c2 = Complex(4, 5)

print(c1+c2)  #  6+8i (This will be printed by the __str__ method)

print("---------\n")

c3 = c1 + c2 
c1.Display()
c2.Display()
print("---------")
c3.Display()

print("\nNow After Multiplication\n")

print(c1*c2)
print("\n---------\n")
c4 = c1 * c2
c1.Display()
c2.Display()
print("---------")
c4.Display()    
    
    
