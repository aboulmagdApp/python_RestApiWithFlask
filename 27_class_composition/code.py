class BookShelf:
    def __init__(self, *books):         # this mean the bookShelf has many books
        self.books = books
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"

book = Book("harry potter")
book2 = Book("python 101")
shelf = BookShelf(book,book2)
print(shelf)