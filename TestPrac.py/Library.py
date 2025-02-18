class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"Title {self.title} Author {self.author} Year {self.year}"
    

class Library:
    def __init__(self):
        bookCase = []
    def addBook(self,book):
        self.bookCase.append(book)
    