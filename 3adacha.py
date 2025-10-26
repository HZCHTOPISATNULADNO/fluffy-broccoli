from numpy.ma.core import append

class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
    def __str__(self):
        return f'{self.title} {self.author}'
class Library:
    def __init__(self, books: list, name: str):
        self.books = books
        self.name = name
    def add_book(self, book: Book):
        self.books.append(book)
    def find_book(self, isbn: int):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return 0
    def remove_book(self, isbn: int):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            print(f"Книга '{book.title}' удалена из библиотеки.")
        else:
            print("Книга с таким isbn не найдена.")
    def list_books(self):
        return [(y.title, y.author) for y in self.books]

book1 = Book("Песня про царя Ивана Васильевича, молодого опричника и удалого купца Калашникова", "Михаил Юрьевич Лермонтов", 876543)
book2 = Book("Бородино", "Милхаил Юрьевич Лермонтов", 456349)
book3 = Book("Штосс", "Михаил Юрьевич Лермонтов", 890324)
library1 = Library([book1, book2], name="San40ous")
library1.add_book(book3)
print(library1.list_books())
print(library1.remove_book(876543))
print(library1.list_books())