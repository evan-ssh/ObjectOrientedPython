#Create program which stores info about doctors in hospital
class Doctor:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"Dr.{self.name} Salary: {self.salary}"