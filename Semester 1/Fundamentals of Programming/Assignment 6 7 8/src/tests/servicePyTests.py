import unittest
from datetime import date

from src.errors.serviceErrors import ServiceError
from src.errors.repoErrors import RepoError

from src.services.bookService import BookService
from src.services.clientService import ClientService
from src.services.rentService import RentService
from src.services.undoService import UndoRedo

from src.domain.book import Book
from src.domain.client import Client
from src.domain.rentals import Rental

from src.repository.repository import Repo

from src.services.validators import *


class BookServiceTests(unittest.TestCase):

    def setUp(self) -> None:
        self._repo = Repo()
        self._validator = BookValidator()
        self._service = BookService(self._repo, self._validator, False)

    def tearDown(self) -> None:
        pass

    def test_addBook(self):

        self.assertEqual(len(self._service()), 0)

        with self.assertRaises(ServiceError):
            self._service.addBook(-1, "", "")

        self._service.addBook(0, "Ifrim Cristian", "Book Title")
        self.assertEqual(len(self._service()), 1)
        self.assertEqual(self._service[0], Book(0, "Ifrim Cristian", "Book Title"))

        with self.assertRaises(RepoError):
            self._service.addBook(0, "Author", "Book")

    def test_callingMethods(self):
        # __getitem__, __call__

        self.assertEqual(self._service(), {})

        with self.assertRaises(RepoError):
            x = self._service[1]

        self._service.addBook(0, "Ifrim Cristian", "Book Title")
        self.assertTrue(self._service[0].getAvailability())

        self.assertEqual(len(self._service()), 1)

    def test_removeItem(self):

        with self.assertRaises(RepoError):
            del self._service[0]

        self._service.addBook(1, "Ifrim Cristian", "Book Title")
        self._service.addBook(2, "Ifrim Cristian", "Book Title")
        self._service.addBook(3, "Ifrim Cristian", "Book Title")

        del self._service[2]

        self.assertEqual(len(self._service()), 2)
        with self.assertRaises(RepoError):
            x = self._service[2]

    def test_searchBookByID(self):

        with self.assertRaises(RepoError):
            x = self._service.searchBookByID(5)

        self._service.addBook(1, "Ifrim Cristian", "Book Title")
        self._service.addBook(2, "Ifrim Cristian", "Book Title")
        self._service.addBook(3, "Ifrim Cristian", "Book Title")

        self.assertEqual(self._service.searchBookByID(2), Book(2, "Ifrim Cristian", "Book Title"))

        self.assertEqual(self._service[1], self._service.searchBookByID(1))

    def test_searchBookByTitle(self):

        with self.assertRaises(RepoError):
            x = self._service.searchBookByTitle("Title")

        self._service.addBook(0, "Autor", "Carte")
        self._service.addBook(1, "Ion Creanga", "Amintiri din Copilarie")
        self._service.addBook(2, "Riot Games", "League of Legends")
        self._service.addBook(3, "Valve", "Counter Strike")

        x = self._service.searchBookByTitle("League")

        self.assertEqual(len(x), 1)

        x = self._service.searchBookByTitle("a")
        self.assertEqual(len(x), 3)

    def test_searchBookByAuthor(self):

        with self.assertRaises(RepoError):
            x = self._service.searchBookByAuthor("Title")

        self._service.addBook(0, "Autor", "Carte")
        self._service.addBook(1, "Ion Creanga", "Amintiri din Copilarie")
        self._service.addBook(2, "Riot Games", "League of Legends")
        self._service.addBook(3, "Valve", "Counter Strike")

        x = self._service.searchBookByAuthor("Riot")

        self.assertEqual(len(x), 1)

        x = self._service.searchBookByAuthor("a")
        self.assertEqual(len(x), 4)

    def test_mostRentedBooks(self):

        self._service.addBook(0, "Autor", "Carte")
        self._service.addBook(1, "Ion Creanga", "Amintiri din Copilarie")
        self._service.addBook(2, "Riot Games", "League of Legends")
        self._service.addBook(3, "Valve", "Counter Strike")

        self._service[3].incRentNumber()
        self._service[3].incRentNumber()
        self._service[3].incRentNumber()

        self._service[1].incRentNumber()

        x = self._service.mostRentedBooks()

        self.assertEqual(x[0], self._service[3])
        self.assertEqual(x[1], self._service[1])
        self.assertEqual(x[2], self._service[0])
        self.assertEqual(x[3], self._service[2])

    def test_mostRentedAuthor(self):

        self._service.addBook(0, "Autor", "Carte")
        self._service.addBook(1, "Ion Creanga", "Amintiri din Copilarie")
        self._service.addBook(2, "Riot Games", "League of Legends")
        self._service.addBook(3, "Valve", "Counter Strike")

        self._service[3].incRentNumber()
        self._service[3].incRentNumber()
        self._service[3].incRentNumber()

        self._service[1].incRentNumber()

        x = self._service.mostRentedAuthor()

        self.assertEqual(x, [("Valve", 3), ("Ion Creanga", 1), ("Autor", 0), ("Riot Games", 0)])

    def test_updateTitle(self):

        self._service.addBook(0, "Autor", "Carte")
        self._service.addBook(1, "Ion Creanga", "Amintiri din Copilarie")
        self._service.addBook(2, "Riot Games", "League of Legends")
        self._service.addBook(3, "Valve", "Counter Strike")

        self._service.updateTitle(0, "Ce frumoasa e dragostea")

        self.assertEqual(self._service[0].title, "Ce frumoasa e dragostea")

        self._service.updateTitle(2, "Valorant")

        self.assertEqual(self._service[2].title, "Valorant")

    def test_updateAuthor(self):

        self._service.addBook(0, "Autor", "Carte")
        self._service.addBook(1, "Ion Creanga", "Amintiri din Copilarie")
        self._service.addBook(2, "Riot Games", "League of Legends")
        self._service.addBook(3, "Valve", "Counter Strike")

        self._service.updateAuthor(0, "Florin Salam")

        self.assertEqual(self._service[0].author, "Florin Salam")

        self._service.updateAuthor(2, "Rito")

        self.assertEqual(self._service[2].author, "Rito")

    def test_updateBook(self):

        self._service.addBook(0, "Autor", "Carte")
        self._service.addBook(1, "Ion Creanga", "Amintiri din Copilarie")
        self._service.addBook(2, "Riot Games", "League of Legends")
        self._service.addBook(3, "Valve", "Counter Strike")

        self._service.updateBook(2, "Valorant", "Rito Games")
        self.assertEqual(self._service[2].author, "Rito Games")
        self.assertEqual(self._service[2].title, "Valorant")

class ClientServiceTests(unittest.TestCase):

    def setUp(self) -> None:
        self._validator = ClientValidator()
        self._repo = Repo()
        self._client = ClientService(self._repo, self._validator, False)

    def tearDown(self) -> None:
        pass

    def test___call__(self):
        self.assertEqual(self._client(), {})

        self._client.addClient(0, "Client")

        self.assertEqual(len(self._client()), 1)

    def test___getitem__(self):

        with self.assertRaises(RepoError):
            x = self._client[1]

        self._client.addClient(0, "Client")
        self.assertEqual(self._client[0].name, "Client")

    def test_addClient(self):

        self.assertEqual(len(self._client()), 0)

        self._client.addClient(0, "Ifrim Cristian")
        self.assertEqual(len(self._client()), 1)

        self.assertEqual(self._client[0], Client(0, "Ifrim Cristian"))

    def test_removeClient(self):

        with self.assertRaises(RepoError):
            del self._client[0]

        self.assertEqual(len(self._client()), 0)

        self._client.addClient(0, "Ifrim Cristian")
        self.assertEqual(len(self._client()), 1)

        self._client.addClient(1, "Ifrim Cristian")
        self.assertEqual(len(self._client()), 2)

        del self._client[0]
        self.assertEqual(len(self._client()), 1)

        with self.assertRaises(RepoError):
            x = self._client[0]

    def test_searchClientByID(self):

        with self.assertRaises(RepoError):
            x = self._client.searchClientByID(5)

        self._client.addClient(0, "Ifrim Cristian")
        self._client.addClient(1, "Ifrim Cristian")
        self._client.addClient(2, "Ifrim Cristian")
        self._client.addClient(3, "Ifrim Cristian")
        self._client.addClient(4, "Ifrim Cristian")
        self._client.addClient(5, "Ifrim Cristian")

        self.assertEqual(self._client.searchClientByID(2), Client(2, "Ifrim Cristian"))

        self.assertEqual(self._client.searchClientByID(4), Client(4, "Ifrim Cristian"))

    def test_searchClientByName(self):
        with self.assertRaises(ServiceError):
            x = self._client.searchClientByName("Test")

        self._client.addClient(0, "Ifrim Cristian")
        self._client.addClient(1, "Ion Creanga")
        self._client.addClient(2, "Mihai Eminescu")
        self._client.addClient(3, "Gabi")
        self._client.addClient(4, "Tarzan")
        self._client.addClient(5, "Cristian")

        x = self._client.searchClientByName("iFriM")

        self.assertEqual(x, [Client(0, "Ifrim Cristian")])

        x = self._client.searchClientByName("Cris")

        self.assertEqual(x, [Client(0, "Ifrim Cristian"), Client(5, "Cristian")])

        x = self._client.searchClientByName("a")

        self.assertEqual(x, [Client(0, "Ifrim Cristian"), Client(1, "Ion Creanga"), Client(2, "Mihai Eminescu"), Client(3, "Gabi"),
                             Client(4, "Tarzan"), Client(5, "Cristian")])

    def test_updateClient(self):

        with self.assertRaises(RepoError):
            self._client.updateClient(25, "Tarzan")

        self._client.addClient(0, "Ifrim Cristian")
        self._client.addClient(1, "Ion Creanga")
        self._client.addClient(2, "Mihai Eminescu")
        self._client.addClient(3, "Gabi")
        self._client.addClient(4, "Tarzan")
        self._client.addClient(5, "Cristian")


        self._client.updateClient(0, "Ifrimel Cristinel")
        self.assertEqual(self._client[0].name, "Ifrimel Cristinel")

        self._client.updateClient(3, "Babi Minune")
        self.assertEqual(self._client[3].name, "Babi Minune")

    def test_mostActiveClient(self):

        self._client.addClient(0, "Ifrim Cristian")
        self._client.addClient(1, "Ion Creanga")
        self._client.addClient(2, "Mihai Eminescu")
        self._client.addClient(3, "Gabi")
        self._client.addClient(4, "Tarzan")
        self._client.addClient(5, "Cristian")

        self._client[5].addDaysRented(40)
        self._client[2].addDaysRented(25)
        self._client[3].addDaysRented(44)

        x = self._client.mostActiveClients()

        self.assertEqual(x[0].getDaysRented(), 44)
        self.assertEqual(x[1].getDaysRented(), 40)
        self.assertEqual(x[2].getDaysRented(), 25)
        self.assertEqual(x[4].getDaysRented(), 0)
        self.assertEqual(x[5].getDaysRented(), 0)

        self.assertEqual(x[0].ID, 3)
        self.assertEqual(x[1].ID, 5)
        self.assertEqual(x[2].ID, 2)
        self.assertEqual(x[3].ID, 0)
        self.assertEqual(x[4].ID, 1)
        self.assertEqual(x[5].ID, 4)

class RentalServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self._repo = Repo()
        self._bookRepo = Repo()
        self._clientRepo = Repo()
        self._rental = RentService(self._repo, self._bookRepo, self._clientRepo, False)

    def tearDown(self) -> None:
        pass

    def test_addRental(self):
        self.assertEqual(self._rental(), {})

        self._bookRepo.add(Book(0, "Ion Creanga", "Amintiri din Copilarie"))
        self._clientRepo.add(Client(0, "Ifrim Cristian"))
        self._rental.addNewRental(0, 0)

        self.assertEqual(len(self._rental()), 1)

        self.assertFalse(self._rental[0].book.getAvailability())
        self.assertTrue(self._rental[0].client.activeRental())
        self.assertEqual(self._rental.items(), 1)
        self.assertEqual(self._rental[0].book.getRentNumber(), 1)

    def test_decItems(self):
        with self.assertRaises(ServiceError):
            self._rental.decItems()

        self._bookRepo.add(Book(0, "Ion Creanga", "Amintiri din Copilarie"))
        self._clientRepo.add(Client(0, "Ifrim Cristian"))
        self._rental.addNewRental(0, 0)
        self._rental.decItems()

        self.assertEqual(self._rental.items(), 0)


class UndoServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.__bookRepo = Repo()
        self.__bookValidator = BookValidator()
        self.__bookService = BookService(self.__bookRepo, self.__bookValidator, False)
        self.__clientValidator = ClientValidator()
        self.__clientRepo = Repo()
        self.__clientService = ClientService(self.__clientRepo, self.__clientValidator, False)
        self.__rentalRepo = Repo()
        self.__rentalService = RentService(self.__rentalRepo, self.__bookRepo, self.__clientRepo, False)

        self.__undoService = UndoRedo(self.__bookService, self.__clientService, self.__rentalService)

        self.__bookService.addBook(0, "Ifrim Cristian", "Viata in Cluj")
        self.__bookService.addBook(1, "Ion Creanga", "Amintiri din Copilarie")
        self.__bookService.addBook(2, "Ion Liviu", "Rebreanu")

        self.__clientService.addClient(0, "Ion")
        self.__clientService.addClient(1, "Vasile")
        self.__clientService.addClient(2, "Andrei")

        self.__rentalService.addInactiveRental(22, 1, 2, date(2020, 2, 25), date(2020, 3, 15))

    def test_undoRedo(self):
        self.__bookService.addBook(3, "Ifrim Cristian", "Carte Noua")
        self.__undoService.addCommandToStack("bAdd", self.__bookService[3])
        self.assertEqual(self.__bookService[3], Book(3, "Ifrim Cristian", "Carte Noua"))
        self.__undoService("undo")

        with self.assertRaises(RepoError):
            x = self.__bookService[3]

        self.__undoService("redo")

        self.assertEqual(self.__bookService[3], Book(3, "Ifrim Cristian", "Carte Noua"))

        self.__rentalService.addNewRental(2, 3)
        self.__undoService.addCommandToStack("rent", [3, 2])
        self.__undoService("undo")

        self.assertFalse(self.__clientService[2].activeRental())

        self.__undoService("redo")

        self.assertTrue(self.__clientService[2].activeRental())

        opList = self.__rentalService.deleteRentalsByClient(2)
        opList.append(["cRemove", Client(2, self.__clientService[2].name,
                                         self.__clientService[2].activeRental(),
                                         self.__clientService[2].getDaysRented())])
        del self.__clientService[2]

        self.__undoService.addCommandToStack("cascade", opList)

        self.__undoService("undo")

        self.assertTrue(self.__clientService[2].activeRental())

        self.__undoService("redo")

        with self.assertRaises(ServiceError):
            x = self.__rentalService.searchRentalByClientID(2)


if __name__ == '__main__':
    unittest.main()
