from src.repository.repository import Repo, RepoError
from src.domain.book import Book
from src.services.validators import BookValidator
from src.services.generators import titleGenerator, authorGenerator

"""
Book service module
This module works only with Book objects and does not interfere with clients functions
There we will only update the state of books such as:
    -Add, remove, update books data(author, title, no. of rents)
    -Search for books by one of their fields
    -Statistics: most rented books, most rented author
    -Undo/redo

"""


class BookService:

    def __init__(self, Repo, Validator, generate):
        """
        Constructor class for the bookService
        :param Repo:
        :param Validator:
        """
        self.__repo = Repo
        self.__validator = Validator

        if generate is True:
            idx = 0
            while (idx < 10):
                self.__repo.add(Book(idx, authorGenerator(), titleGenerator()))

                idx += 1


    def __call__(self): #tested
        """
        Returns the repo dictionary
        :return:
        """
        return self.__repo()

    def __getitem__(self, item): #tested
        """
        This function gets the item repo[key] from repository
        :param item:
        :return:
        """
        return self.__repo[item]

    def __delitem__(self, key): #tested
        """
        Deletes the item repo[key] from the repo dict
        :param key:
        :return:
        """
        del self.__repo[key]

    def addBook(self, bID, bAuthor, bName, isAvailable = True, rentNumber = 0): #tested
        """
        Add a book to the repo
        1. Create a new book
        2. Validate data
        3. Add to repo
        :param bID: the id of the book
        :param bAuthor: the author of the book
        :param bName: the title of the book
        :return: --
        """

        book = Book(bID, bAuthor, bName, isAvailable, rentNumber)  # 1
        self.__validator.validateBook(book)  # 2
        self.__repo.add(book)  # 3


    def searchBookByID(self, bID): #tested
        """
        This functions returns the book with id = bID
        :param bID:
        :return:
        """
        if bID not in self.__repo():
            raise RepoError(f'The entity with ID: {bID} is not in repo.')

        return self.__repo[bID]

    def searchBookByTitle(self, bTitle): #tested
        l = []
        for item in self.__repo():
            if bTitle.lower() in self.__repo[item].title.lower():
                l.append(self.__repo[item])

        if len(l) == 0:
            raise RepoError(f"No book was found that it's title contain {bTitle}.")

        return l

    def searchBookByAuthor(self, bTitle): #tested
        l = []
        for item in self.__repo():
            if bTitle.lower() in self.__repo[item].author.lower():
                l.append(self.__repo[item])
        if len(l) == 0:
            raise RepoError(f"No book was found that it's author contain {bTitle}.")
        return l

    def mostRentedBooks(self): #tested
        """
        Statistics for the most rented books
        :return:
        """
        books = list(self.__repo.getList())
        books.sort(reverse = True)

        return books

    def mostRentedAuthor(self): #tested
        l = dict()

        for item in self.__repo():
            if self.__repo[item].author not in l:
                l[self.__repo[item].author] = self.__repo[item].getRentNumber()
            else:
                l[self.__repo[item].author] += self.__repo[item].getRentNumber()

        authorList = list(l.items())
        authorList.sort(key=lambda x: x[1], reverse=True)

        return authorList


    def updateTitle(self, bID, bTitle): #tested
        """
        Updates the title of a given book
        :param bID:
        :param bTitle:
        :return:
        """
        if bID not in self.__repo():
            raise RepoError(f'The entity with ID: {bID} is not in repo.')

        self.__repo[bID].title = bTitle

    def updateAuthor(self, bID, bAuthor): #tested
        """
        Updates the author of a given book
        :param bID:
        :param bAuthor:
        :return:
        """
        if bID not in self.__repo():
            raise RepoError(f'The entity with ID: {bID} is not in repo.')

        self.__repo[bID].author = bAuthor

    def updateBook(self, bID, bTitle, bAuthor): #tested
        """
        Updates the title and the author of the book
        :param bID:
        :param bTitle:
        :param bAuthor:
        :return:
        """
        self.updateAuthor(bID, bAuthor)
        self.updateTitle(bID, bTitle)

