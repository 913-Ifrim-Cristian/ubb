from src.domain.book import Book
from src.domain.client import Client
from datetime import date

class Rental:
    def __init__(self, id, book, client, rentDate, returnDate = date(1, 1, 1)):
        self.__rentID = id
        self.__client = client
        self.__book = book
        self.__rentDate = rentDate
        self.__returnDate = returnDate

    @property
    def ID(self):
        return self.__rentID

    @ID.setter
    def ID(self, value):
        self.__rentID = value

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        self.__client = value

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        self.__book = value

    @property
    def rent(self):
        return self.__rentDate

    @rent.setter
    def rent(self, value):
        self.__rentDate = value

    @property
    def unrent(self):
        return self.__returnDate

    @unrent.setter
    def unrent(self, value):
        self.__returnDate = value

    def __str__(self):
        format = "%d/%m/%Y"
        return f"Rental ID: {self.__rentID}, Book: {self.__book.title}, Client: {self.__client.name}, Rent date: {self.__rentDate.strftime(format)}, Return date: {self.__returnDate.strftime(format)}"

