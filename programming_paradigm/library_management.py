# programming_paradigm/library_management.py

class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        self.title = title              # public attribute
        self.author = author            # public attribute
        self._is_checked_out = False    # private attribute (by convention)

    def check_out(self):
        """Mark the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Represents a collection of books in the library."""

    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title, if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"{title} has been checked out."
        return f"Sorry, {title} is not available."

    def return_book(self, title):
        """Return a book by title, making it available again."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"{title} has been returned."
        return f"{title} was not checked out."

    def list_available_books(self):
        """Print all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
