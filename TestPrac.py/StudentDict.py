class Student:
    def __init__(self,name):
        self.name = name
        self.grades = {}
    
    def addGrade(self,subject,grade):
       self.grades[subject] = grade

    def delGrade(self,subject):
        if subject in self.grades:
            del self.grades[subject]
    def updateGrade(self,subject,grade):
        if subject in self.grades:
            self.grades[subject] = grade
    def showGrade(self):
        print(f"{self.name}'s Grades")
        for subject,grade in self.grades.items():
            print(f"{subject} - Grade {grade}")

if __name__ == "__main__":
    student = Student("Eric")
    student.addGrade("English",65)
    student.addGrade("Math",75)
    student.addGrade("Physics",85)
    student.showGrade()