import unittest
from src.domain.book import Book
from src.domain.client import Client
from src.domain.rentals import Rental
from datetime import date


class domainTests(unittest.TestCase):

    def setUp(self) -> None:
        self.__book = Book(1, "Ifrim Cristian", "Book Title")
        self.__client = Client(1, "Ion Creanga")
        self.__rental = Rental(0, self.__book, self.__client, date.today())

    def tearDown(self) -> None:
        pass

    def test_bookData(self):
        self.assertEqual(self.__book.ID, 1)
        self.assertEqual(self.__book.title, "Book Title")
        self.assertEqual(self.__book.author, "Ifrim Cristian")

        self.assertTrue(self.__book.getAvailability())
        self.assertEqual(self.__book.getRentNumber(), 0)

        self.assertEqual(str(self.__book), "Book ID: 1, Author: Ifrim Cristian, Title: Book Title, No. of rents: 0, is Available: True")

        self.__book.toggleIsAvailable()
        self.assertFalse(self.__book.getAvailability())

        self.__book.incRentNumber()
        self.assertEqual(self.__book.getRentNumber(), 1)

        testBook = Book(2, "La la la", "Vita de vie")
        testBook.incRentNumber()
        testBook.incRentNumber()
        testBook.incRentNumber()

        statement = self.__book < testBook
        self.assertTrue(statement)

        for i in range(5):
            self.__book.incRentNumber()

        statement = self.__book > testBook
        self.assertTrue(statement)

        self.__book.ID = 5
        self.assertEqual(self.__book.ID, 5)

        self.__book.title = "De la inceput"
        self.assertEqual(self.__book.title, "De la inceput")

        self.__book.author = "Gheorghe"
        self.assertEqual(self.__book.author, "Gheorghe")

    def test_clientData(self):
        self.assertEqual(self.__client.ID, 1)
        self.assertEqual(self.__client.name, "Ion Creanga")
        self.assertFalse(self.__client.activeRental())
        self.assertEqual(self.__client.getDaysRented(), 0)

        self.__client.toggleActiveRental()
        self.assertTrue(self.__client.activeRental())

        self.__client.addDaysRented(50)
        self.assertEqual(self.__client.getDaysRented(), 50)

        self.assertEqual(str(self.__client), "Client ID: 1, Name: Ion Creanga, Rent Days: 50, Active Rent: True")

        self.__client.id = 2
        self.assertEqual(self.__client.id, 2)

        self.__client.name = "Lalea"
        self.assertEqual(self.__client.name, "Lalea")

        testClient = Client(3, "Corona")
        testClient.addDaysRented(100)

        statement = self.__client < testClient
        self.assertTrue(statement)

        statement = self.__client > testClient
        self.assertFalse(statement)




    def test_rentalData(self):
        self.assertEqual(self.__rental.ID, 0)
        self.assertEqual(self.__rental.client, self.__client)
        self.assertEqual(self.__rental.book, self.__book)
        self.assertEqual(self.__rental.rent.strftime("%d/%m/%Y"), date.today().strftime("%d/%m/%Y"))
        self.assertEqual(self.__rental.unrent, date(1, 1, 1))

        self.__rental.unrent = date.today()
        self.assertEqual(self.__rental.unrent.strftime("%d/%m/%Y"), date.today().strftime("%d/%m/%Y"))

        self.assertEqual(str(self.__rental), "Rental ID: 0, Book: Book Title, Client: Ion Creanga, Rent date: 03/12/2021, Return date: 03/12/2021")

        self.__rental.rent = date(2021, 10, 23)
        self.assertEqual(self.__rental.rent, date(2021, 10, 23))

        self.__rental.ID = 5
        self.assertEqual(self.__rental.ID, 5)

        self.__rental.client = Client(1, "Viorel")
        self.assertEqual(self.__rental.client, Client(1, "Viorel"))

        self.__rental.book = Book(9, "Ashe", "Lol")
        self.assertEqual(self.__rental.book, Book(9, "Ashe", "Lol"))



if __name__ == '__main__':
    unittest.main()
