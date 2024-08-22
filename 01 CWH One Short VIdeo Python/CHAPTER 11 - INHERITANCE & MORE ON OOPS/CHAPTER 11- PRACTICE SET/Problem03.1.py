# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salaryAfterIncrement(self):
        return  self.salary + self.salary
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.salary = salary 
        

e = Employee("Gaurav Sah", 12)  
print(e.salaryAfterIncrement) # 12 + 12 = 24

e.salaryAfterIncrement = 15  # This will change the value of salary
print(e.salaryAfterIncrement)  # 15 + 15 = 30









