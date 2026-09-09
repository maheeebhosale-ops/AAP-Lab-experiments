
# Experiment 1: Library Management System using OOP

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def return_book(self):
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"{self.name} (ID: {self.patron_id}) - Books held: {len(self.borrowed_books)}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.isbn] = book
        print(f"Book added: {book.title}")

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron registered: {patron.name}")

    def borrow_book(self, patron_id, isbn):
        patron = self.patrons.get(patron_id)
        book = self.books.get(isbn)
        if not patron or not book:
            print("Invalid patron ID or ISBN.")
        elif patron.borrow_book(book):
            print(f"{patron.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, patron_id, isbn):
        patron = self.patrons.get(patron_id)
        book = self.books.get(isbn)
        if patron and book and patron.return_book(book):
            print(f"{patron.name} returned '{book.title}'")
        else:
            print("Return failed. Check patron ID and ISBN.")

    def display_books(self):
        print("\n--- Library Books ---")
        for book in self.books.values():
            print(book)

    def display_patrons(self):
        print("\n--- Registered Patrons ---")
        for patron in self.patrons.values():
            print(patron)


def main():
    library = Library()

    print("=== LIBRARY MANAGEMENT SYSTEM ===\n")

    library.add_book(Book("The Alchemist", "Paulo Coelho", "101"))
    library.add_book(Book("Wings of Fire", "A P J Abdul Kalam", "102"))
    library.add_book(Book("Python Crash Course", "Eric Matthes", "103"))

    library.register_patron(Patron("Neil Hole", "P01"))
    library.register_patron(Patron("Riya Sharma", "P02"))

    library.display_books()

    print("\n--- Borrowing ---")
    library.borrow_book("P01", "101")
    library.borrow_book("P02", "101")
    library.borrow_book("P02", "103")

    library.display_books()
    library.display_patrons()

    print("\n--- Returning ---")
    library.return_book("P01", "101")

    library.display_books()
    library.display_patrons()


if __name__ == "__main__":
    main()
