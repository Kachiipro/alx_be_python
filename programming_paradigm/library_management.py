# library_management

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def is_available(self):
        """Checks if the book is available."""
        return not self._is_checked_out

    def is_checkout(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for i in self._books:
            if i.title == title:
                if i._is_checked_out == False:
                    i.is_checkout()
                else:
                    print(f"{title} is already checked out.")

    def return_book(self, title):
        for i in self._books:
            if i.title == title:
                if i._is_checked_out == True:
                    i.return_book()
                else:
                    return f"{title} is already returned."

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are available.")
