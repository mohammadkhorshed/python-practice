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
    
    def find_book_by_year(self, year):
        book_list = [book for book in self.books if book.year == year]
        if not book_list:
            print(f"No book 'published in {year}' is available in the library!")
            return
        print(f"Book(s) published in {year}: ")
        for idx, book in enumerate(book_list):
            print(f"{idx + 1}. {book}")
    
    def find_book_by_genre(self, genre):
        book_list = [book for book in self.books if book.genre.lower() == genre.lower()]
        if not book_list:
            print(f"No book of {genre} genre, is available in the library!")
            return
        print(f"Book(s) of {genre} genre: ")
        for idx, book in enumerate(book_list):
            print(f"{idx + 1}. {book}")

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_available = True
    
    def __str__(self):
        return f"{self.title} [{self.genre}] by {self.author} published in {self.year} - {'Available' if self.is_available else 'Not available'}"
    
    def __repr__(self):
        return f"Book(title = '{self.title}', author = '{self.author}', year = {self.year}, genre = {self.genre}, available = {self.is_available})"

class BookNotFoundException(Exception):
    pass



if __name__ == "__main__":

    my_library = Library()

    # Create books
    book_1 = Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy")
    book_2 = Book("1984", "George Orwell", 1949, "Dystopian")
    book_3 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy")
    book_4 = Book("The Alchemist", "Paulo Coelho", 1988, "Philosophy")
    book_5 = Book("Frankenstein", "Mary Shelley", 1818, "Science Fiction")
    book_6 = Book("Animal Farm", "George Orwell", 1945, "Dystopian")
    book_7 = Book("A Game of Thrones", "George R.R. Martin", 1996, "Fantasy")

    # Add books
    my_library.add_book(book_1)
    my_library.add_book(book_2)
    my_library.add_book(book_3)
    my_library.add_book(book_4)
    my_library.add_book(book_5)
    my_library.add_book(book_6)
    my_library.add_book(book_7)

    # Display available books
    my_library.display_available_books()

    # Borrow book
    my_library.borrow_book("1984")

    # Again display available books
    my_library.display_available_books()

    # Find book by author
    my_library.find_book_by_author("George Orwell")
    
    # Find book by year
    my_library.find_book_by_year(1988)

    # Find book by genre
    my_library.find_book_by_genre("Fantasy")

    # Return book
    my_library.return_book("1984")