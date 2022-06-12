import json

class Book:
    def __init__(self, id, author, title, isAvailable = True, rentNumber = 0):
        self.__bookID = id
        self.__title = title
        self.__author = author
        self.__isAvailable = isAvailable
        self.__rentNumber = rentNumber

    @property
    def ID(self):
        return self.__bookID

    @ID.setter
    def ID(self, value):
        self.__bookID = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    def getAvailability(self):
        return self.__isAvailable

    def toggleIsAvailable(self):
        self.__isAvailable = not self.__isAvailable

    def getRentNumber(self):
        return self.__rentNumber

    def incRentNumber(self):
        self.__rentNumber += 1

    def decRentNumber(self):
        self.__rentNumber -= 1

    def __gt__(self, other):
        return self.__rentNumber > other.getRentNumber()

    def __lt__(self, other):
        return self.__rentNumber < other.getRentNumber()

    def __eq__(self, other):
        return  self.__bookID == other.ID and\
                self.__title == other.title and\
                self.__author == other.author and\
                self.__rentNumber == other.getRentNumber() and\
                self.__isAvailable == other.getAvailability()

    def __str__(self):
        return f'Book ID: {self.__bookID}, Author: {self.__author}, Title: {self.__title}, No. of rents: {self.__rentNumber}, is Available: {self.__isAvailable}'