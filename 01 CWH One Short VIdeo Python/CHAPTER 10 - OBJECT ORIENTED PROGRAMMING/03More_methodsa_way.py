class Employee:
    
    greet = "Good Morning"
    
    def __init__(self, name, age, salary, g = "Hi/Hello"):  # This is a constructor or dunder method
        self.name = name
        self.age = age
        self.salary = salary
        self.greet = g

    def display(self):  
        print(self.greet)
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)   
        
    
    
    
    
obj = Employee("Gaurav", 21, 1000000)
obj.display()

# Output
    # Hi/Hello
    # Name:  Gaurav
    # Age:  21
    # Salary:  1000000

print("\n")
obj2 = Employee("Monu", 22, 2000000, "Hello Sir,")
obj2.display()
print(obj2.greet)

# Output
    # Hello Sir,
    # Name:  Monu
    # Age:  22
    # Salary:  2000000
    # Hello Sir,
