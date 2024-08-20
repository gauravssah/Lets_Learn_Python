class Employee: 
    name = "Gaurav"  # This is a class variable or Attribute
    Language = "Python"
    Salary = 1000000
    
obj = Employee()

print(obj.Language)
print(obj.name)
print(obj.Salary)

obj.Departement = "IT"  # This is an instance variable
print(obj.Departement)
    