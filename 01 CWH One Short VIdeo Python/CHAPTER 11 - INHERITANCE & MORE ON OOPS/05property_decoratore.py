class Employee:
    a = 1
    
    @property
    def name(self):
        return f"{self.fname}\n{self.lname}"
    
    @name.setter
    def name(self, value):
        # fname, lname = value.split(" ")
        # self.fname = fname
        # self.lname = lname
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.name = "Gaurav Sah"
print(e.name)



