# 3. Create a class ‘Employee’ and add salary and increment properties to it.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("The name of the employee is: ",self.name, " and his salary is: ",self.salary)
        
    def increment(self):
        self.salary = self.salary * 1.5

e = Employee("Gaurav Sah", 1200000000)
e.display()
e.increment()
e.display()



