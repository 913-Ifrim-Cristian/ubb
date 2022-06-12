from src.domain.book import Book
from src.domain.client import Client
from src.repository.repository import Repo
from src.services.clientService import ClientService
from src.services.bookService import BookService

class UI:

    def __init__(self, bookService, clientService, rentService, undoService):
        self.__bookService = bookService
        self.__clientService = clientService
        self.__rentService = rentService
        self.__undoService = undoService
        self.__commandDict = {
                                "+": self.addCommand,
                                "-": self.removeCommand,
                                "=": self.updateCommand,
                                "l": self.listCommand,
                                ">": self.rentCommand,
                                "<": self.unrentCommand,
                                "s": self.searchCommand,
                                "?": self.statisticsCommand,
                                "u": self.undoCommand,
                                "r": self.redoCommand
                             }

    def printMenu(self):
        print("Hello, user! Please select an option from below:")
        print("------------------------------------------------")
        print(">>> Manage clients and books")
        print("\t+ \t-> Add a client(c) or a book(b).")
        print("\t- \t-> Remove a client(c) or a book(b).")
        print("\t= \t-> Update a client(c) or a book(b).")
        print("\tl \t-> List clients(c) or books(b).")
        print(">>> Rent or return a book")
        print("\t> \t-> Rent a book.")
        print("\t< \t-> Return a book.")
        print(">>> Search clients or books")
        print("\ts \t-> Search specific clients(c) or books(b).")
        print(">>> Statistics")
        print("\t? \t-> Display statistics about most rented books(b), most active clients(c) or most rented author(a).")
        print(">>> Undo/Redo operations")
        print("\tu \t-> Undo the last performed operation.")
        print("\tr \t-> Redo the last performed operation.")
        print(">>> Extra")
        print("\tx \t -> Exit the program")
        print("------------------------------------------------")

    def printList(self, l):
        for item in l:
            print(item)

    def start(self):
        self.printMenu()
        while True:
            option = input(">>> Option: ")

            if option == "x":
                return

            if option == "rentals":
                for item in self.__rentService():
                    print(self.__rentService[item])

            elif option not in self.__commandDict:
                print("Invalid option!\n")
            else:
                try:
                    self.__commandDict[option]()
                except Exception as e:
                    print(e)
    """
    The first functionality
    """
    def addCommand(self):
        option = input(">>> Option(b -> book, c -> client): ")

        if option == "b":
            id = int(input("Please enter the ID of the book: "))
            title = input("Please enter the title of the book: ")
            author = input("Please enter the author of the book: ")

            self.__bookService.addBook(id, title, author)
            self.__undoService.addCommandToStack("bAdd", Book(id, author, title))

            print(f"Book with ID: {id} added succesfully!\n")

        elif option == "c":
            id = int(input("Please enter the ID of the client: "))
            name = input("Please enther the name of the client: ")

            self.__clientService.addClient(id, name)
            self.__undoService.addCommandToStack("cAdd", Client(id, name))

            print(f"Client with ID: {id} added succesfully!\n")

    def commitClientRemoval(self, clientID):
        opList = self.__rentService.deleteRentalsByClient(clientID)
        opList.append(["cRemove", Client(clientID, self.__clientService[clientID].name,
                                         self.__clientService[clientID].activeRental(),
                                         self.__clientService[clientID].getDaysRented())])
        del self.__clientService[clientID]

        self.__undoService.addCommandToStack("cascade", opList)

    def commitBookRemoval(self, bookID):
        opList = self.__rentService.deleteRentalsByBook(bookID)
        opList.append(["bRemove", Book(bookID, self.__bookService[bookID].author, self.__bookService[bookID].title,
                                       self.__bookService[bookID].getAvailability(),
                                       self.__bookService[bookID].getRentNumber())])

        del self.__bookService[bookID]

        self.__undoService.addCommandToStack("cascade", opList)

    def removeCommand(self):
        # TODO: Cascading remove

        option = input("Please enter what do you want to remove(b -> Book, c -> Client): ")

        if option == "b":
            bookID = int(input("Please enter the ID of the book you want to delete: "))

            self.commitBookRemoval(bookID)

            print(f"Succesfuly deleted the book with ID: {bookID}!\n")


        elif option == "c":
            clientID = int(input("Please enter the ID of the client you want to delete: "))

            self.commitClientRemoval(clientID)

            print(f"Succesfuly deleted the client with ID: {clientID}!\n")


        else:
            print("Invalid option!")
    def updateCommand(self):

        """
        It is pointless to modify the ID of a book/client as it is only an identifier.
        Major fields are title, author(Book), name(client)
        :return:
        """

        option = input("What do you want to update(b -> Book, c -> Client): ")

        if option == 'b':
            bookID = int(input("Please enter the id of the book you want to edit: "))
            self.commitBookUpdate(bookID)

            print(f"Succesfuly updated book with ID: {bookID}!\n")

        elif option == 'c':
            clientID = int(input("Please enter the id of the client you want to edit: "))
            self.commitClientUpdate(clientID)

            print(f"Succesfuly updated client with ID: {clientID}!\n")
        else:
            print("Incorrect option!\n")

    def commitBookUpdate(self, bookID):

        option = int(input("Please select what do you want to modify:\n1.Title\n2.Author\n3.Both\n>>>"))

        if option == 1:
            newTitle = input(f"Please enter the new title of the book(ID: {bookID}): ")
            self.__undoService.addCommandToStack("bUpdate", [1, bookID, self.__bookService[bookID].title, newTitle])
            self.__bookService.updateTitle(bookID, newTitle)

        elif option == 2:
            newTitle = input(f"Please enter the new author of the book(ID: {bookID}): ")
            self.__undoService.addCommandToStack("bUpdate", [2, bookID, self.__bookService[bookID].author, newTitle])
            self.__bookService.updateAuthor(bookID, newTitle)

        elif option == 3:

            newTitle = input(f"Please enter the new title of the book(ID: {bookID}): ")
            newAuthor = input(f"Please enter the new author of the book(ID: {bookID}): ")

            self.__undoService.addCommandToStack("bUpdate", [3, bookID, self.__bookService[bookID].title, newTitle,
                                                             self.__bookService[bookID].author, newAuthor])
            self.__bookService.updateBook(bookID, newTitle, newAuthor)

        else:
            print("Incorrect option!\n")

    def commitClientUpdate(self, clientID):

        name = input(f"Please enter the new name of the client(ID: {clientID}): ")

        self.__undoService.addCommandToStack("cUpdate", [clientID, self.__clientService[clientID].name, name])

        self.__clientService.updateClient(clientID, name)

    def listCommand(self):
        option = input(">>> Option(b -> book, c -> client): ")

        if option == "b":
            for item in self.__bookService():
                print(self.__bookService[item])
        elif option == "c":
            for item in self.__clientService():
                print(self.__clientService[item])

    """
    The second functionality
    """
    def rentCommand(self):
        clientID = int(input("Please enter the ID of the client that rents a book: "))
        bookID = int(input("Please enter the ID of the book to be rented: "))

        self.__rentService.addNewRental(clientID, bookID)
        self.__undoService.addCommandToStack("rent", [bookID, clientID])

        print("Rental added succesfully!\n")

    def unrentCommand(self):
        option = input("How do you want to return the book?(b -> book id, c -> client id): ")

        if option == "b":
            id = int(input("Please enter the ID of the book: "))
            rental = self.__rentService.returnBook(id, 1)

            print(rental)
            self.__undoService.addCommandToStack("unrent", rental)
            print(f"Book from rental: {rental} returned succesfully!\n")
        elif option == "c":
            id = int(input("Please enter the ID of the client: "))
            rental = self.__rentService.returnBook(id, 2)


            print(rental)
            self.__undoService.addCommandToStack("unrent", rental)
            print(f"Book from rental: {rental} returned succesfully!\n")

        else:
            print("Invalid option!")


    """
    The third functionality
    """
    def searchCommand(self):
        option = input("What do you want to search(b -> Book, c -> Client): ")

        if option == 'b':
            self.commitSearchBook()

        elif option == 'c':
            self.commitSearchClient()

    def commitSearchBook(self):
        option = int(input("Please select your search criterion:\n1.ID\n2.Title\n3.Author\n>>> "))

        if option == 1:
            ID = int(input("Please enter the ID of the book: "))
            print(self.__bookService[ID])

        elif option == 2:
            title = input("Please enter a title or a key word: ")

            l = self.__bookService.searchBookByTitle(title)

            self.printList(l)

        elif option == 3:
            author = input("Please enter an author or a key word: ")

            l = self.__bookService.searchBookByAuthor(author)

            self.printList(l)

    def commitSearchClient(self):
        option = int(input("Please select your search criterion:\n1.ID\n2.Name\n>>> "))

        if option == 1:
            ID = int(input("Please enter the ID of the client: "))
            print(self.__clientService[ID])

        elif option == 2:
            title = input("Please enter a title or a key word: ")

            l = self.__clientService.searchClientByName(title)

            self.printList(l)

    """
    The fourth functionality
    """
    def statisticsCommand(self):
        option = input("Please select one of the following:\na.Most rented author\nb.Most rented books\nc.Most active clients\n>>>")

        if option == "a":
            l = self.__bookService.mostRentedAuthor()

            for item in l:
                print(f"Author: {item[0]} was rented {item[1]} times.")

        elif option == "b":
            l = self.__bookService.mostRentedBooks()

            self.printList(l)

        elif option == "c":
            l = self.__clientService.mostActiveClients()

            self.printList(l)


    """
    The fifth functionality
    """
    def undoCommand(self):
        self.__undoService("undo")
        print("Undo operation went succesfully!")
    def redoCommand(self):
        self.__undoService("redo")
        print("Redo operation went succesfully!")
