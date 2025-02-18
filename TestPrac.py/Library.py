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

if __name__ == "__main__":
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("Moby Dick", "Herman Melville", 1851)
    library.addBook(book1)
    library.addBook(book2)
    print("Current Books In Library")
    for book in library:
     print(book)
    library.removeBook("Moby Dick")
    print("Current Books In Library")
    for book in library:
     print(book)