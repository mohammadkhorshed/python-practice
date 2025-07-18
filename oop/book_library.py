class Library:
    def __init__(self):
        pass

    def add_book(self):
        pass

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def display_available_books(self):
        pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def __str__(self):
        return f"{self.title} by {self.author} - {'Available' if self.is_available else 'Not available'}"
    
    def __repr__(self):
        return f"Book(title = '{self.title}', author = '{self.author}', available = {self.is_available})"