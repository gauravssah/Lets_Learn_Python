class Employee:
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        
    def display(self):
        print("The name of the employee is: ",self.name, " and his salary is: ",self.salary)
    
class Programmer(Employee):
    def showLanguage(self):
        print(f"He is a Programmer and his favourite language is {self.language}")
        

a = Programmer("Ramesh", 50000, "Python")
print("\n")
a.display()
a.showLanguage()
print("\n")


