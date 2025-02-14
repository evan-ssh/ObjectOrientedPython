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
    def __iter__(self):
        for doc in self.doctors:
            yield doc
        

if __name__ == "__main__":        
 d1 = Doctor("Eric","3232323")
 d2 = Doctor("John","40343443")
 s1 = Surgeon("Timmy","3434242423","Trauma")
 s2 = Surgeon("Kenny","34343","Heart")
 hospital = Hospital()
 hospital.addDoc(d1)
 hospital.addDoc(d2)
 hospital.addDoc(s1)
 hospital.addDoc(s2)
 for doc in hospital:
    print(doc)  
                 