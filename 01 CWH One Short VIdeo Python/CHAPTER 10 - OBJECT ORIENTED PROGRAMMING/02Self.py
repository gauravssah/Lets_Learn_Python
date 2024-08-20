class Employee:
    language = "Python"
    salary = 1000000
    
    def __init__(self):
        print("I am creatin an object, and automatically call me")
    
    def display(self):
        print("Language: ",self.language)
        print("Salary: ",self.salary)  
        
    # At the place of self we can use any name Like rr kk etc.
    def greet(self):  # Why Self Explain - It is used to refer to the current instance of the class.
        print("Good Morning")
        
    @staticmethod
    def hello():
        print("This will Not Take Self.")
        

Gaurav = Employee()
Gaurav.greet()
Gaurav.display()
Gaurav.hello()

print("\n")
Monu = Employee()
Monu.greet()
Monu.display()










