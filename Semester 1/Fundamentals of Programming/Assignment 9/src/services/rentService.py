from src.errors.serviceErrors import ServiceError
from src.domain.rentals import Rental
from src.services.generators import dateGenerator
from datetime import date
from random import randint


class RentService:
    def __init__(self, rentRepo, bookRepo, clientRepo, generator):
        self.__rentRepo = rentRepo
        self.__bookRepo = bookRepo
        self.__clientRepo = clientRepo
        self.__noOfItems = len(self.__rentRepo)

        if generator is True:
            while(self.__noOfItems < 14):
                d1, d2 = dateGenerator()
                book = randint(0, 9)
                client = randint(0, 9)

                self.__bookRepo[book].incRentNumber()
                self.__clientRepo[client].addDaysRented((d2-d1).days)

                self.__rentRepo.add(Rental(self.__noOfItems, book, client, d1, d2))
                self.__noOfItems += 1

    def __call__(self):
        return self.__rentRepo()

    def __delitem__(self, key):
        del self.__rentRepo[key]

    def __getitem__(self, item):
        return self.__rentRepo[item]

    def items(self):
        return self.__noOfItems

    def decItems(self):
        if self.__noOfItems == 0:
            raise ServiceError("Cannot decrease anymore!")
        self.__noOfItems -= 1

    def addNewRental(self, clientID, bookID):

        if self.__bookRepo[bookID].getAvailability() is False:
            raise ServiceError(f"Book with ID: {bookID} is not available!")

        if self.__clientRepo[clientID].activeRental() is True:
            raise ServiceError(f"Client with ID: {clientID} already has a rented book!")

        today = date.today()
        self.__bookRepo[bookID].toggleIsAvailable()
        self.__bookRepo[bookID].incRentNumber()
        self.__clientRepo[clientID].toggleActiveRental()
        self.__rentRepo.add(Rental(self.__noOfItems, bookID, clientID, today))
        self.__noOfItems += 1

    def addInactiveRental(self, id, bookID, clientID, rent, unrent):

        if id in self.__rentRepo():
            raise ServiceError(f"Rental with ID: {id} already exists!")
        self.__rentRepo.add(Rental(id, bookID, clientID, rent, unrent))
        self.__bookRepo[bookID].incRentNumber()
        if unrent != date(1, 1, 1):
            self.__clientRepo[clientID].addDaysRented((unrent-rent).days)
        #else:
            #self.__clientRepo[clientID].toggleActiveRental()

    def searchRentalByBookID(self, bookID):

        for item in self.__rentRepo():
            if self.__rentRepo[item].book == bookID and self.__rentRepo[item].unrent == date.fromisoformat("0001-01-01"):
                return self.__rentRepo[item]

        raise ServiceError(f"No active rental that has the book with ID {bookID} was found!")

    def searchRentalByClientID(self, clientID):

        for item in self.__rentRepo():
            if self.__rentRepo[item].client == clientID and self.__rentRepo[item].unrent == date.fromisoformat("0001-01-01"):
                return self.__rentRepo[item]

        raise ServiceError(f"No active rental that has the client with ID {clientID} was found!")

    def returnBook(self, ID, searchType):
        if searchType == 1:
            rental = self.searchRentalByBookID(ID)
        else:
            rental = self.searchRentalByClientID(ID)

        today = date.today()
        rental.unrent = today

        self.__bookRepo[rental.book].toggleIsAvailable()
        self.__clientRepo[rental.client].toggleActiveRental()

        self.__clientRepo[rental.client].addDaysRented((rental.unrent - rental.rent).days)

        return rental.ID

    def deleteRentalsByClient(self, clientID):
        opList = []
        for item in list(self.__rentRepo()):
            if self.__rentRepo[item].client == clientID:
                if self.__rentRepo[item].unrent != date(1, 1, 1):
                    cID = self.__rentRepo[item].client
                    self.__clientRepo[cID].addDaysRented(-(self.__rentRepo[item].unrent - self.__rentRepo[item].rent).days)

                self.__bookRepo[self.__rentRepo[item].book].decRentNumber()
                opList.append(["delete", [item, self.__rentRepo[item].book, self.__rentRepo[item].client,
                                          self.__rentRepo[item].rent, self.__rentRepo[item].unrent]])
                del self.__rentRepo[item]

        return opList

    def deleteRentalsByBook(self, clientID):
        opList = []
        for item in list(self.__rentRepo()):
            if self.__rentRepo[item].book == clientID:
                if self.__rentRepo[item].unrent != date(1, 1, 1):
                    cID = self.__rentRepo[item].client
                    self.__clientRepo[cID].addDaysRented(-(self.__rentRepo[item].unrent - self.__rentRepo[item].rent).days)

                self.__bookRepo[self.__rentRepo[item].book].decRentNumber()
                opList.append(["delete", [item, self.__rentRepo[item].book, self.__rentRepo[item].client,
                                          self.__rentRepo[item].rent, self.__rentRepo[item].unrent]])

                del self.__rentRepo[item]

        return opList