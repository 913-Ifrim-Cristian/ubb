from src.domain.book import Book
from src.domain.client import Client
from src.domain.rentals import Rental

from src.repository.repository import Repo

from src.errors.repoErrors import RepoError

from src.services.bookService import BookService
from src.services.clientService import ClientService
from src.services.rentService import RentService
from src.services.validators import *

def test_BookService():

    bookRepo = Repo()
    bookValidator = BookValidator()
    bookService = BookService(bookRepo, bookValidator)

    bookService.addBook(25, "Ion Creanga", "Amintiri din Copilarie")
    assert bookService[25].ID == 25
    assert bookService[25].author == "Ion Creanga"
    assert bookService[25].title == "Amintiri din Copilarie"

    bookService.addBook(26, "Tata", "Mama")

    del bookService[2]

    try:
        x = bookService[2]
        assert False
    except RepoError as re:
        assert str(re) == "The entity with ID: 2 is not in repo."

    book = bookService.searchBookByID(25)
    assert book.ID == 25
    assert book.author == "Ion Creanga"
    assert book.title == "Amintiri din Copilarie"


    """
    Testing updateBook also tests updateTitle, updateAuthor!!!
    """
    bookService.updateBook(25, "Lalea", "Floare")
    assert bookService[25].title == "Lalea"
    assert bookService[25].author == "Floare"


def test_ClientService():

    clientRepo = Repo()
    clientValidator = ClientValidator()
    clientService = ClientService(clientRepo, clientValidator)

    clientService.addClient(25, "Ion Creanga")
    assert clientService[25].ID == 25
    assert clientService[25].name == "Ion Creanga"

    clientService.addClient(26, "Tata")

    del clientService[2]

    try:
        x = clientService[2]
        assert False
    except RepoError as re:
        assert str(re) == "The entity with ID: 2 is not in repo."

    book = clientService.searchClientByID(25)
    assert book.ID == 25
    assert book.name == "Ion Creanga"


    clientService.updateClient(25, "Lalea")
    assert clientService[25].name == "Lalea"


test_BookService()
test_ClientService()