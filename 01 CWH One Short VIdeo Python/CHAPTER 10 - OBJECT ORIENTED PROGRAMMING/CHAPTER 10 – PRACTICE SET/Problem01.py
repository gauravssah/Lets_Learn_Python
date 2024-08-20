# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.

class Programmer:
    def __init__(self, name, JobType, salery, lan, filed):
        self.name = name
        self.jobType = JobType
        self.salery = salery
        self.language = lan
        self.field = filed
    
    def info(self):
        print(f"Name: {self.name}")
        print(f"Job Type: {self.jobType}")
        print(f"Salery: {self.salery}")
        print(f"Working Language: {self.language}")
        print(f"Working Field: {self.field}")
        

employ1 = Programmer("Gaurav Sah", "Tech", "12000000", "Python", "Ai Ml Eng.")
employ1.info()


