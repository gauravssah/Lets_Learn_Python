class Company:
    def __init__(self, company_name, company_location):
        self.company_name = company_name
        self.company_location = company_location
    
    def display(self):
        print("The name of the company is: ",self.company_name, " and his location is: ",self.company_location)
    
class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def Employee_display(self):
        print("The name of the employee is: ",self.name, " and his salary is: ",self.salary)
        
class Programmer(Employee, Company):
    def __init__(self, name, salary, company_name, company_location):
        Employee.__init__(self, name, salary)
        Company.__init__(self, company_name, company_location)
    
    def Programmer_display(self):
        print("The name of the programmer is: ",self.name, " and his salary is: ",self.salary, " and his company name is: ",self.company_name, " and his company location is: ",self.company_location)
        
a = Programmer("Ramesh", 50000, "Infosys", "Pune")
print("\n")
a.display()
a.Employee_display()
a.Programmer_display()
print("\n")
  