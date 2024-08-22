class Company:
    def __init__(self, Company_Name, Company_Location):
        self.Company = Company_Name
        self.Location = Company_Location
    
    def ShowCompany(self):
        print(f"The name of the comapny is : {self.Company}, Its Located At : {self.Location}")
        
class Employee(Company):
    def __init__(self, employee_name ,Company_Name, Company_Location):
        self.name = employee_name
        super().__init__(Company_Name, Company_Location)
        
    def Employ_Info(self):
        print(f"Name of Employee is : {self.name}")
        

class Programmer(Employee):
    def __init__(self,prog_language ,employee_name, Company_Name, Company_Location):
        self.language = prog_language
        super().__init__(employee_name, Company_Name, Company_Location)

    def programmer(self):
        print(f"His programming langi=uage is : {self.language}")
        
    def AllDetails(self):
        print(f"Name is : {self.name}, his company name is : {self.Company} At {self.Location}, and his programming language is : {self.language}")

        
    
a = Programmer("python", "Gaurav", "Google", "USA")
a.AllDetails()

a.ShowCompany()
a.Employ_Info()
a.programmer()







