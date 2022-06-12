from src.domain.book import Book
from src.domain.client import Client

def test_Book():
    carte = Book(1, "Vali Vijelie", "La ceas vengo")

    assert carte.ID == 1
    assert carte.title == "La ceas vengo"
    assert carte.author == "Vali Vijelie"
    assert carte.getRentNumber() == 0
    assert carte.getAvailability() == True

    carte.ID = 2
    assert carte.ID == 2

    carte.title = "Zece"
    assert carte.title == "Zece"

    carte.author = "Florin Chilian"
    assert carte.author == "Florin Chilian"

    carte.incRentNumber()
    assert carte.getRentNumber() == 1

    carte.toggleIsAvailable()
    assert carte.getAvailability() == False

    assert str(carte) == "Book ID: 2, Author: Florin Chilian, Title: Zece, No. of rents: 1"

def test_Client():

    client = Client(1, "Ifrim Cristian")

    assert client.ID == 1
    assert client.name == "Ifrim Cristian"

    client.ID = 2
    assert client.ID == 2

    client.name = "Steaua Bucuresti"
    assert client.name == "Steaua Bucuresti"

    assert str(client) == "Client ID: 2, Name: Steaua Bucuresti"


def domain_runTests():
    test_Book()
    test_Client()

domain_runTests()