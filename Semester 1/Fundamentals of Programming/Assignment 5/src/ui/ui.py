from src.domain.domain import Book
from src.services.services import Service
from src.services.tests import runTests

class UI:
    def __init__(self, service):
        self._menuCommands = {
                              "+": self.addBook,
                              "l": self.listBooks,
                              "f": self.filterBooks,
                              "u": self.undoOperation
                             }
        self.services = service

    def _printMenu(self):
        print("Welcome user! Please select a command!")
        print("--------------------------------------")
        print("# -> +:\tAdd a book to the list")
        print("# -> l:\tDisplay the list of books")
        print("# -> f:\tFilter the list so that book titles starting with a given word are deleted from the list.")
        print("# -> u:\tUndo the last operation that modified program data.")
        print("# -> x:\tExit the program.")
        print("--------------------------------------")

    def addBook(self):
        isbn = input("Please enter the ISBN code of the book: ")
        author = input("Please enter the author of the book, if unknown leave blank: ")
        title = input("Please enter the title of the book, if untitled leave blank: ")

        book = Book(isbn, author, title)
        self.services.add(book)

        print("Succesfully added " + str(book) + "!\n")

    def undoOperation(self):
        self.services.undo()

        print("The undo operation has been performed!\n")

    def listBooks(self):
        for item in self.services.getList():
            print(item)
        print("\n")

    def start(self):
        while(True):
            self._printMenu()
            option = input("Please select one option from the above: ").strip().lower()

            if option == 'x':
                print("Have a nice day!")
                return

            if option not in self._menuCommands:
                print("Error! Please enter a valid command!\n")
            else:
                try:
                    self._menuCommands[option]()
                except ValueError as ve:
                    print(ve)

    def filterBooks(self):
        word = input("Please enter a word to filter the books starting with it: ")
        self.services.filter(word.strip().lower())

        print("Succesfully filtered the list!\n")

def main():

    service = Service()
    ui = UI(service)

    """
    try:
        runTests()
        print("All tests succesfully passed!")

    except ValueError as ve:
        print(ve)
    """
    ui.start()

main()