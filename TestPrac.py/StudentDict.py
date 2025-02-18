class Student:
    def __init__(self,name):
        self.name = name
        self.grades = {}
    
    def addGrade(self,subject,grade):
       self.grades[subject] = grade

