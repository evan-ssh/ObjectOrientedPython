class ListManger:
    def __init__(self):
        self.list = []
    
    def addToList(self,item):
        self.list.append(item)

    def RemoveFromList(self,item):
        if item in self.list:
            self.list.remove(item)
        else:
            print("Item not in list")
    
    def searchList(self,item):
        if item in self.list:
            return self.list.index(item)
        else:
            return "Item not in list"