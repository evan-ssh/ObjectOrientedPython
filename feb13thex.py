#Create program which stores info about doctors in hospital
class Doctor:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"Dr.{self.name} Salary: {self.salary}"

class Surgeon(Doctor):
    def __init__(self,name,salary,specialty):
        Doctor.__init__(self,name,salary)
        self.specialty = specialty
    def __str__(self):
        return f"Dr.{self.name} Salary: {self.salary} Specialty: {self.specialty}"
    
class Hospital:
    def __init__(self):
        self.doctors = []
    def addDoc(self,doctor):
        self.doctors.append(doctor)
                 