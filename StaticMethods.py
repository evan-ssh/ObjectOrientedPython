class Math:
    @staticmethod#not changing staying the same
    def add5(x):
        return x + 5
    @staticmethod#A static method can be called withput an object for that class
    def add10(x):
        return x + 10
    @ staticmethod
    def multiply(x, y):#you dont need to pass self through these
        return x * y
    @staticmethod
    def pr():
        print("run")
    
#m = math() not needed
print(Math.add5(5))
print(Math.add10(10))
Math.pr(Math.multiply(10,5))
Math.pr()
