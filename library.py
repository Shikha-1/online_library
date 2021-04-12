class Library:
    def __init__(self, list_of_books):
        self.list_of_books = list_of_books
    def display_book(self):
        print("Books present in the Library are:")
        books = self.list_of_books.keys()
        for i in books:
            print(f"\t* {i}")
    def lend_book(self):
        name = input("Enter Your Name: ")
        book = input("Enter Book Name: ")
        if book in self.list_of_books.keys():
            self.list_of_books.pop(book)
            print(f"You have been issued '{book}'. Please keep it safe and return it within 30 days")
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False
    def add_book(self):
        name = input("Enter Your Name: ")
        book = input("Enter Book Name: ")
        self.list_of_books.update({book:name})
        print(f"Thanks! Your book '{book}' has been added.")
    def return_book(self):
        name = input("Enter Your Name: ")
        book = input("Enter Book Name: ")
        self.list_of_books.update({name:book})
        print(f"Your book '{book}' has been returned successfully! Hope you enjoyed it.")
    def person(self):
        book = input("Enter Book Name: ")
        if book in self.list_of_books.keys():
            print(f"{self.list_of_books.get(book)} has this '{book}' now")
        else:
            print("Sorry, This book is not available in our library!")

if __name__ == "__main__":
    online_library = Library({
            "the truth":"ram",
            "the fiction":"shyam",
            "the hero":"raj",
            "villain n king":"kallu",
            "one night @ coffee shop":"mallu"
        })
    while True:
        print('''\n ====== Welcome to Online Library ======
        Please choose an option:
        1. List of all the books
        2. Request a book
        3. Add a book
        4. Return a book
        5. Know who owns the book you want
        6. Exit the Library
        ''')
        choice = int(input("Your Choice: "))
        if choice == 1:
            online_library.display_book()
        elif choice == 2:
            online_library.lend_book()
        elif choice == 3:
            online_library.add_book()
        elif choice == 4:
            online_library.return_book()
        elif choice == 5:
            online_library.person()
        elif choice == 6:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Plz enter a valid input!")