class Student:
    def __init__(self,name):
        self.name = name
        self.grades = {}
    
    def addGrade(self,subject,grade):
       self.grades[subject] = grade

    def delGrade(self,subject):
        if subject in self.grades:
            del self.grades[subject]