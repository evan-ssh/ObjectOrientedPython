class Task:
    def __init__(self, id, name, description, completed=False):
        self.id = id
        self.name = name
        self.description = description
        self.completed = completed

    def markDone(self):
        self.completed = True

    def __str__(self):
        return f"{self.name} = {'Completed' if self.completed else 'Not completed'}"

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def addTask(self, task):
        self.tasks[task.id] = task

    def markTaskCompleted(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].markDone()

    def displayCompleted(self):
        for task in self.tasks.values():
            if task.completed:
                print(task)

    def __iter__(self):
        for task in self.tasks.values():
            yield task

if __name__ == "__main__":
    task1 = Task(1, "Finish Python Assignment", "Practice For test")
    task2 = Task(2, "Finish Java Assignment", "Few Questions Left")
    task3 = Task(3, "Clean Room", "Do TODAY")

    toDO = ToDoList()
    toDO.addTask(task1)
    toDO.addTask(task2)
    toDO.addTask(task3)

    print("All Tasks")
    for task in toDO:
     print(task)

    toDO.markTaskCompleted(2)

    print("\nCompleted Tasks")
    toDO.displayCompleted()
