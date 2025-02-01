""" 
add book and author and page 
add dvd and magazines with other details
give those books

"""
class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Copies: {self.copies})"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            self.books[book.isbn].copies += book.copies
        else:
            self.books[book.isbn] = book
        print(f"Book added: {book}")

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def search_book(self, title=None, author=None):
        results = []
        for book in self.books.values():
            if (title and title.lower() in book.title.lower()) or (author and author.lower() in book.author.lower()):
                results.append(book)
        return results

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books.values():
                print(book)

    def borrow_book(self, isbn):
        if isbn in self.books and self.books[isbn].copies > 0:
            self.books[isbn].copies -= 1
            print(f"You have borrowed: {self.books[isbn].title}")
        elif isbn in self.books:
            print(f"Sorry, all copies of {self.books[isbn].title} are currently borrowed.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def return_book(self, isbn):
        if isbn in self.books:
            self.books[isbn].copies += 1
            print(f"Thank you for returning: {self.books[isbn].title}")
        else:
            print(f"No book found with ISBN {isbn}. Please check the details.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, isbn, copies)
            library.add_book(book)

        elif choice == "2":
            isbn = input("Enter book ISBN to remove: ")
            library.remove_book(isbn)

        elif choice == "3":
            title = input("Enter book title (or leave blank): ").strip() or None
            author = input("Enter book author (or leave blank): ").strip() or None
            results = library.search_book(title, author)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(book)
            else:
                print("No books found matching the criteria.")

        elif choice == "4":
            print("\nBooks in Library:")
            library.display_books()

        elif choice == "5":
            isbn = input("Enter book ISBN to borrow: ")
            library.borrow_book(isbn)

        elif choice == "6":
            isbn = input("Enter book ISBN to return: ")
            library.return_book(isbn)

        elif choice == "7":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

        