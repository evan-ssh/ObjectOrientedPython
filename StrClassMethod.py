class Student:
    def __init__(self,name,grade,id,school):

        self.name = name
        self.grade = grade
        self.id = id
        self.school = school

    def __str__(self):
        return f"{self.name} {self.grade}"
    def Student_Id(self):
        return f"{self.id} {self.school}"
mary = Student("Mary","A+","12334","123School")
print(f"{str(mary)} {mary.Student_Id()}")#<__main__.Student object at 0x00000223E3B6EC10>