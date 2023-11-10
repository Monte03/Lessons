
class Book:
    def __init__(self, title, author, isbn, year, pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.pages = pages
        self.available = True
    
    # інформація про книгу
    def info_book(self):
        st_available = 'Доступна' if self.available else 'Не доступна'
        info = """
        Назва: {self.title}
        Автор: {self.author}
        ISBN: {self.isbn}
        Рік видання: {self.year}
        Кількість сторінок: {self.pages}
        Статус наявності: {st_available}
        """
        print(info)
    
    # статус наявності книги
    def availability_status(self, new_status):
        self.available = new_status
        print(f"Статус наявності книги змінено на {'Доступна' if self.available else 'Не доступна'}")
    
class Reader:
    def __init__(self, name, age, reader_id):
        self.name = name
        self.age = age
        self.reader_id = reader_id
        self.borrowed_books = []
    
    # взяти книгу
    def take_book(self, book):
        if book.available:
            pass
    
    # повернути книгу
    def return_book(self):
        pass
    
    # список взятих книг
    def list_take_book(self):
        pass
    
class Library:
    def __init__(self, books, readers):
        self.books = books
        self.readers = readers
    
    # додавання однієї книги
    def add_one_book(self):
        pass
    
    # додавання одного користувача 
    def add_one_user(self):
        pass
    
    # видача книги користувачеві
    def issuing_book_user(self):
        pass
    
    # отримання взятої книги 
    def receiving_book_taken(self):
        pass
    