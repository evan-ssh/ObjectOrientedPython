class Student:
    def __init__(self,name:str,age:int,grade:int):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self,name:str,max_students:int):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True#if true
        return False#if not
    
    def get_average_grade(self):
        value:int = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Tim",20,60)
s2 = Student("Bill",30,79)
s3 = Student("Jill",19,98)

course = Course("SoftwareDev",2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.add_student(s3))#returns false because the course only takes two students
print(course.get_average_grade())