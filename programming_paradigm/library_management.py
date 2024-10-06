# library_management

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def is_checkout(self):
        self._is_checked_out = True

    def is_return(self):
        self._is_checked_out = False


class Library(Book):
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def list_available_books(self):

        for i in self._books:
            if i._is_checked_out == False:
                print(f"{i.title} by {i.author}")

    def check_out_book(self, title):
        for i in self._books:
            if i.title == title:
                if i._is_checked_out == False:
                    i.is_checkout()
                else:
                    print(f"{title} is already checked out.")
        print(f"{i.title} is not in the library")

    def return_book(self):
        for i in self._books:
            if i.title == title:
                if i._is_checked_out == True:
                    i.is_return()
                else:
                    print(f"{title} is already returned.")
        print(f"{i.title} is not in the library")
