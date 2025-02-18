class Task:
    def __init__(self,id,name,description,completed):
        self.id = id
        self.name = name
        self.description = description
        self.completed = False

    def markDone(self):
        self.completed = True

    def __str__(self):
        return f"{self.name} = {'Completed' if self.completed else 'Not completed'}"
    
class ToDoList:
    def __init__(self):
        self.tasks = {}

    def addTask(self,task):
        self.tasks[task.id] = task

         
    
