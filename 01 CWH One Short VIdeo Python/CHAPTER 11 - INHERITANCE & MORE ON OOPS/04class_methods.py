class Employee:
    a = 1
    
    @classmethod
    def show(cls):  # class method, cls may be self or cls
        print(f"The value of class variable is : {cls.a}")
        
a = Employee()
a.show()  # The value of class variable is : 1
a.a = 10
a.show()  # The value of class variable is : 1
 
