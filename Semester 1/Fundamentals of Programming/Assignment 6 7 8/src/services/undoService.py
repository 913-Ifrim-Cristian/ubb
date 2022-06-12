from src.errors.serviceErrors import ServiceError
from src.domain.rentals import Rental
from datetime import date
"""
Undo/Redo service class
This takes care of the undo/redo functionality
Functions that need to be able to undo/redo:
    -Add, remove, update books/clients
    -Rent/return a book
"""

class UndoRedo:

    def __init__(self, bookService, clientService, rentalService):
        self.__bookService = bookService
        self.__clientService = clientService
        self.__rentalService = rentalService

        self.__commandStackTop = -1
        self.__commandStack = []

        self.__undoDict = {
            "bAdd": self.undoAddBook,
            "bRemove": self.undoRemoveBook,
            "bUpdate": self.undoUpdateBook,
            "cAdd": self.undoAddClient,
            "cRemove": self.undoRemoveClient,
            "cUpdate": self.undoUpdateClient,
            "rent": self.undoRentBook,
            "delete": self.undoDeleteRent,
            "unrent": self.undoUnrentBook,
            "cascade": self.undoCascadeRemove,
        }

        self.__redoDict = {
            "bAdd": self.redoAddBook,
            "bRemove": self.redoRemoveBook,
            "bUpdate": self.redoUpdateBook,
            "cAdd": self.redoAddClient,
            "cRemove": self.redoRemoveClient,
            "cUpdate": self.redoUpdateClient,
            "rent": self.redoRentBook,
            "delete": self.redoDeleteRent,
            "unrent": self.redoUnrentBook,
            "cascade": self.redoCascadeRemove,
        }

    def addCommandToStack(self, action, object):
        self.__commandStackTop += 1
        self.__commandStack.insert(self.__commandStackTop, [action, object])
        del self.__commandStack[self.__commandStackTop+1:]

    def getLastOperation(self):
        operation = self.__commandStack[self.__commandStackTop]
        self.__commandStackTop -= 1
        return operation

    def getLastOpCommand(self, operation):
        return operation[0]

    def getLastOpObject(self, operation):
        return operation[1]

    def getNextOperation(self):
        operation = self.__commandStack[self.__commandStackTop + 1]
        self.__commandStackTop += 1
        return operation

    def __call__(self, option):
        if option == "undo":
            if self.__commandStackTop == -1:
                raise ServiceError("There is nothing to undo.")

            lastOperation = self.getLastOperation()

            action = self.getLastOpCommand(lastOperation)
            object = self.getLastOpObject(lastOperation)

            self.__undoDict[action](object)

        elif option == "redo":
            if self.__commandStackTop == len(self.__commandStack) - 1:
                raise ServiceError("There is nothing to redo.")

            nextOperation = self.getNextOperation()

            action = self.getLastOpCommand(nextOperation)
            object = self.getLastOpObject(nextOperation)

            self.__redoDict[action](object)

    def undoAddBook(self, book):
        del self.__bookService[book.ID]

    def undoRemoveBook(self, book):
        self.__bookService.addBook(book.ID, book.author, book.title, book.getAvailability(), book.getRentNumber())

    def undoCascadeRemove(self, operations):
        newOperations = operations[:]
        while len(newOperations) > 0:
            operation = newOperations.pop()
            action = self.getLastOpCommand(operation)
            object = self.getLastOpObject(operation)

            self.__undoDict[action](object)

    def undoUpdateBook(self, book):

        if book[0] == 1:
            self.__bookService.updateTitle(book[1], book[2])
        elif book[0] == 2:
            self.__bookService.updateAuthor(book[1], book[2])
        elif book[0] == 3:
            self.__bookService.updateBook(book[1], book[2], book[4])

    def undoAddClient(self, client):
        del self.__clientService[client.ID]

    def undoRemoveClient(self, client):
        self.__clientService.addClient(client.ID, client.name, client.activeRental(), client.getDaysRented())

    def undoUpdateClient(self, params):
        self.__clientService.updateClient(params[0], params[1])

    def undoRentBook(self, params):
        rental = self.__rentalService.searchRentalByBookID(params[0])
        self.__rentalService[rental.ID].book.toggleIsAvailable()
        self.__rentalService[rental.ID].book.decRentNumber()
        self.__rentalService[rental.ID].client.toggleActiveRental()
        self.__rentalService.decItems()
        del self.__rentalService[rental.ID]

    def undoDeleteRent(self, params):
        """
        params[0] -> Rental ID
        params[1] -> Book ID
        params[2] -> Client ID
        params[3] -> Rent Date
        params[4] -> Return Date
        :param params:
        :return:
        """
        self.__rentalService.addInactiveRental(params[0], params[1], params[2], params[3], params[4])

    def undoUnrentBook(self, rental):

        self.__rentalService[rental].book.toggleIsAvailable()
        self.__rentalService[rental].client.toggleActiveRental()

        self.__rentalService[rental].client.addDaysRented(-
                                        (self.__rentalService[rental].unrent - self.__rentalService[rental].rent).days)

        self.__rentalService[rental].unrent = date(1, 1, 1)


    """
    REDO FUNCTIONALITY
    """
    def redoAddBook(self, book):
        self.undoRemoveBook(book)

    def redoRemoveBook(self, book):
        self.undoAddBook(book)

    def redoCascadeRemove(self, operations):
        for item in operations:
            action = self.getLastOpCommand(item)
            object = self.getLastOpObject(item)

            self.__redoDict[action](object)

    def redoUpdateBook(self, book):

        if book[0] == 1:
            self.__bookService.updateTitle(book[1], book[3])
        elif book[0] == 2:
            self.__bookService.updateAuthor(book[1], book[3])
        elif book[0] == 3:
            self.__bookService.updateBook(book[1], book[3], book[5])

    def redoAddClient(self, client):
        self.undoRemoveClient(client)

    def redoRemoveClient(self, client):
        self.undoAddClient(client)

    def redoUpdateClient(self, params):
        self.__clientService.updateClient(params[0], params[2])

    def redoRentBook(self, params):
        self.__rentalService.addNewRental(params[1], params[0])

    def redoDeleteRent(self, params):
        item = params[0]
        if self.__rentalService[item].unrent != date(1, 1, 1):
            self.__rentalService[item].client.addDaysRented(
                -(self.__rentalService[item].unrent - self.__rentalService[item].rent).days)

        self.__rentalService[item].book.decRentNumber()
        del self.__rentalService[item]

    def redoUnrentBook(self, rental):

        self.__rentalService.returnBook(self.__rentalService[rental].book.ID, 1)