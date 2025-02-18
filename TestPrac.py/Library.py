class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"Title {self.title} Author {self.author} Year {self.year}"
    

class Library:
    def __init__(self):
        self.bookCase = []
    def addBook(self,book):
        self.bookCase.append(book)
    def removeBook(self,book):
        for books in self.bookCase:
            if books.title == book:
                self.bookCase.remove(books)
    def findBook(self,author):
        for book in self.bookCase:
            if book.author == author:
                return book
    def __iter__(self):
        for book in self.bookCase   :
            yield book

