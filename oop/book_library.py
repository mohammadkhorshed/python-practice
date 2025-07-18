class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"You have borrowed {book.title}")
                    return
                else:
                    print(f"{book.title} is not available!")
                    return
        raise BookNotFoundException(f"Book with the title '{title}' is not found in the library!")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print(f"Thank you for returning {book.title}")
                    return
                else:
                    print(f"{book.title} wasn't borrowed!")
                    return
        raise BookNotFoundException(f"Book with the title '{title}' is not found in the library!")

    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available == True]
        if not available_books:
            print("No book is available in the library!")
            return
        print("Available books: ")
        for idx, book in enumerate(available_books):
            print(f"{idx + 1}. {book}")
    
    def find_book_by_author(self, author):
        book_list = [book for book in self.books if book.author.lower() == author.lower()]
        if not book_list:
            print(f"No book by {author.title()} is available in the library!")
            return
        print(f"Book(s) by {author.title()}: ")
        for idx, book in enumerate(book_list):
            print(f"{idx + 1}. {book}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def __str__(self):
        return f"{self.title} by {self.author} - {'Available' if self.is_available else 'Not available'}"
    
    def __repr__(self):
        return f"Book(title = '{self.title}', author = '{self.author}', available = {self.is_available})"

class BookNotFoundException(Exception):
    pass
