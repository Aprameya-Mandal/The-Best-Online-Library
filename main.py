#  Best code for library class version---1.3
class lib:
    def __init__(self, name_of_lib, lst_books):
        self.lib_name = name_of_lib
        self.books = list(lst_books)
        self.till_lent_books = list()
        self.till_lent_books_owner_names = list()
        self.passwords = list()

    def remove_usual(self):
        for i in self.books:
            if i.strip() == '':
                self.books.remove(i)

    def display_books(self):
        print(f"Library name: {self.lib_name}\n")
        if self.books != list():
            print("Books")
            self.books.sort()
            for i in self.books:
                print(i)
        else:
            print("There is no book in the library..")

        if self.till_lent_books != list():
            bookLens = [len(i) for i in self.till_lent_books]
            req_space = max(bookLens) + 18
            for no, i in enumerate(self.till_lent_books):
                if no == 0:
                    print(f"\nAlready Lent books {' ' * (req_space - 18)} Owner names")
                bookowner = self.till_lent_books_owner_names[self.till_lent_books.index(i)]
                booklen = len(i)
                print(f"{i}{' ' * (req_space - booklen)}  {bookowner}\n")
        else:
            print("There is no book lent in the library..\n")

    def lend_book(self, name_of_book, user_name, password):
        if name_of_book in self.books:
            self.books.remove(name_of_book)
            self.till_lent_books.append(name_of_book)
            self.till_lent_books_owner_names.append(user_name)
            self.passwords.append(password)
        else:
            print(f"Lending unsuccessful. There is no book named {name_of_book} in the library available\n"
                  "If you want to know who owns the book at the present moment you can run the display_books function"
                  "\nif you are sure that any other person already lent the book from the library\n")

    def add_book(self, name_of_book):
        if name_of_book not in self.books and name_of_book not in self.till_lent_books:
            self.books.append(name_of_book)
        else:
            print(f"Adding unsuccessful. There is already a book named {name_of_book} available or lent")

    def return_book(self, name_of_book, user_name, password):
        if name_of_book in self.till_lent_books and self.till_lent_books_owner_names[
                self.till_lent_books.index(name_of_book)] == user_name and self.passwords[
                self.till_lent_books.index(name_of_book)] == password:
            self.till_lent_books.remove(name_of_book)
            self.till_lent_books_owner_names.remove(user_name)
            self.books.append(name_of_book)
        else:
            print(f"Returning unsuccessful. There is no book lent named {name_of_book}"
                  f" or check the spelling of the owner name or the password you gave")


def main():
    print("Welcome to the virtual library center...")
    print("Note: If you add a book named ''(blank) that would be removed...")
    print("Initializing...")
    print("Creating a object...")
    print("Enter the name of the library...")
    name = input()
    a2 = lib(name, list())
    YesOrNo = input("Do you want to add any book in the library at the first(Y/N): ")
    YesOrNo = YesOrNo.lower()
    if YesOrNo == 'y':
        noOfBooks = input("Enter the no. of books: ")
        if noOfBooks.isnumeric():
            noOfBooks = int(noOfBooks)
        else:
            while not noOfBooks.isnumeric():
                noOfBooks = input("Enter the no. of books: ")
                if noOfBooks.isnumeric():
                    noOfBooks = int(noOfBooks)
                    break
        for i in range(1, noOfBooks + 1):
            a = input("Enter the name of the book: ")
            if a not in a2.books:
                a2.books.append(a)
                print(f"Book {i}/{noOfBooks}")
            else:
                print(f"There is already a book named {a} in the book...")
                a = input("Enter the name of the book: ")
                if a not in a2.books:
                    a2.books.append(a)
                    print(f"Book {i}/{noOfBooks}")
                    continue
                while a in a2.books:
                    print(f"There is already a book named {a} in the book...")
                    a = input("Enter the name of the book: ")
                    if a not in a2.books:
                        a2.books.append(a)
                        print(f"Book {i}/{noOfBooks}")
                        break
    elif YesOrNo == 'n':
        a2 = lib(name, list())
    else:
        while YesOrNo != 'y' or YesOrNo != 'n':
            print("Please enter a valid option...")
            YesOrNo = input("Do you want to add any book in the library at the first(Y/N): ")
            YesOrNo = YesOrNo.lower()
            if YesOrNo == 'y':
                noOfBooks = input("Enter the no. of books: ")
                if noOfBooks.isnumeric():
                    noOfBooks = int(noOfBooks)
                else:
                    while not noOfBooks.isnumeric():
                        noOfBooks = input("Enter the no. of books: ")
                        if noOfBooks.isnumeric():
                            noOfBooks = int(noOfBooks)
                            break
                for i in range(1, noOfBooks + 1):
                    a = input("Enter the name of the book: ")
                    if a not in a2.books:
                        a2.books.append(a)
                        print(f"Book {i}/{noOfBooks}")
                    else:
                        print(f"There is already a book named {a} in the book...")
                        a = input("Enter the name of the book: ")
                        if a not in a2.books:
                            a2.books.append(a)
                            print(f"Book {i}/{noOfBooks}")
                            continue
                        while a in a2.books:
                            print(f"There is already a book named {a} in the book...")
                            a = input("Enter the name of the book: ")
                            if a not in a2.books:
                                a2.books.append(a)
                                print(f"Book {i}/{noOfBooks}")
                                break
                break
            elif YesOrNo == 'n':
                a2 = lib(name, list())
                break
    while True:
        a = a2
        a.remove_usual()
        print("Press 1 for displaying the books")
        print("Press 2 for lending a book")
        print("Press 3 for donating or adding a book")
        print("Press 4 for returning a book")
        choice = input()
        if choice == '1':
            a.display_books()
        elif choice == '2':
            name = input("Enter the name of the book: ")
            user_name = input("Enter the user name: ")
            password = input('Enter a password for the book (For avoiding abuse): ')
            a.lend_book(name, user_name, password)
        elif choice == '3':
            name = input("Enter the name of the book: ")
            a.add_book(name)
        elif choice == '4':
            name = input("Enter the name of the book: ")
            user_name = input("Enter the user name: ")
            password = input('Now enter the password you gave for the book: ')
            a.return_book(name, user_name, password)
        else:
            print("Enter a valid option...")
            continue


if __name__ == '__main__':
    try:
        main()

    except Exception as e:
        print(e, "\nNot a valid option...")