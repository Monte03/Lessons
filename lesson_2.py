
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
        info = f"""
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
    
    # користувач бере книгу
    def take_book(self, book):
        if book.available:
            book.availability_status(False)
            self.borrowed_books.append(book)
            print(f"{self.name} взяв(-ла) книгу '{book.title}'")
        else:
            print(f"Вибачте, книга '{book.title}' вже взята")

    # користувач повертає книгу
    def return_book(self, book):
        if book in self.borrowed_books:
            book.availability_status(True)
            self.borrowed_books.remove(book)
            print(f"{self.name} повернув книгу '{book.title}'")
        else:
            print(f"{self.name}, ви не маєте книгу '{book.title}' у вас")

    # вивід списку взятих книг
    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} має на руках наступні книги:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print(f"{self.name} не має на руках жодної книги")


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    # додавання однієї книги до бібліотеки
    def add_one_book(self, book):
        self.books.append(book)
        print(f"Додано книгу '{book.title}' до бібліотеки")

    # додавання одного читача до бібліотеки
    def add_one_user(self, reader):
        self.readers.append(reader)
        print(f"Зареєстровано читача: {reader.name}")

    # даємо книгу користувачеві 
    def issuing_book_user(self, reader, book):
        reader.take_book(book)

    # приймає повернену книгу від читача
    def receiving_book_taken(self, reader, book):
        reader.return_book(book)


book1 = Book("Пригоди Аліси в Країні Див", "Льюїс Керролл", "978-3-16-148410-0", 1865, 200)
book2 = Book("Майстер та Маргарита", "Михайло Булгаков", "978-5-17-022032-0", 1966, 360)


reader1 = Reader("Володя", 40, 1)
reader2 = Reader("Марія", 30, 2)

library = Library()

library.add_one_book(book1)
library.add_one_book(book2)

library.add_one_user(reader1)
library.add_one_user(reader2)

reader1.list_borrowed_books()

library.issuing_book_user(reader1, book1)
reader1.list_borrowed_books()