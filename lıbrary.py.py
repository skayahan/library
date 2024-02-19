class Book:
    def __init__(self, title, author, release_year, pages):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Release Year: {self.release_year}, Pages: {self.pages}"

class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            book = Book(*book_info)
            print(book)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully!")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        lines = self.file.read().splitlines()
        books = [Book(*line.split(',')) for line in lines]

        new_books = [book for book in books if book.title != title_to_remove]

        self.file.truncate(0)
        self.file.seek(0)
        for book in new_books:
            book_info = f"{book.title},{book.author},{book.release_year},{book.pages}\n"
            self.file.write(book_info)

        print("Book removed successfully!")

    def search_book(self):
        search_title = input("Enter the title of the book to search: ")

        self.file.seek(0)
        lines = self.file.read().splitlines()
        books = [Book(*line.split(',')) for line in lines]

        found_books = [book for book in books if book.title.lower() == search_title.lower()]

        if found_books:
            for book in found_books:
                print(book)
        else:
            print("Book not found.")

    def update_book(self):
        update_title = input("Enter the title of the book to update: ")

        self.file.seek(0)
        lines = self.file.read().splitlines()
        books = [Book(*line.split(',')) for line in lines]

        for i, book in enumerate(books):
            if book.title == update_title:
                books[i].title = input("Enter new title: ")
                books[i].author = input("Enter new author: ")
                books[i].release_year = input("Enter new release year: ")
                books[i].pages = input("Enter new number of pages: ")
                break

        self.file.truncate(0)
        self.file.seek(0)
        for book in books:
            book_info = f"{book.title},{book.author},{book.release_year},{book.pages}\n"
            self.file.write(book_info)

        print("Book updated successfully!")

# Create Library object
lib = Library()

# Menu
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Search Book")
    print("5) Update Book")
    print("6) Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        lib.search_book()
    elif choice == "5":
        lib.update_book()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
