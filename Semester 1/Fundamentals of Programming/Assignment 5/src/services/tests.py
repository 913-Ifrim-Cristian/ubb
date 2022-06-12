from src.services.services import *


def test_hasDigits():
    assert hasDigits("test1") is True
    assert hasDigits("steaua") is False
    assert hasDigits("dinamoegal0") is True
    assert hasDigits("1234") is True

def test_checkISBN():
        assert checkISBN("forta-steaua") is False
        assert checkISBN("000-0-0000-0000-0") is True
        assert checkISBN("aaa-a-aaaa-aaaa-a") is False
        assert checkISBN("00a-0-1234-5555-0") is False

def test_serviceAdd():

    service = Service()

    assert len(service.getList()) == 10 # testing if it has 10 values at start up

    service.add(Book("333-1-4444-5555-2", "Corona Virus", "Lockdown"))
    lastElem = service.getList()[-1]
    assert lastElem.isbn == "333-1-4444-5555-2" and lastElem.author == "Corona Virus" and lastElem.title == "Lockdown"

    service.add(Book("334-1-4544-5255-2", "Liviu Rebreanu", "Ion"))
    lastElem = service.getList()[-1]
    assert lastElem.isbn == "334-1-4544-5255-2" and lastElem.author == "Liviu Rebreanu" and lastElem.title == "Ion"

    service.add(Book("212-4-2211-1234-6", "", ""))
    lastElem = service.getList()[-1]
    assert lastElem.isbn == "212-4-2211-1234-6" and lastElem.author == "Anonymous" and lastElem.title == "Untitled"

def runTests():
    test_hasDigits()
    test_checkISBN()
    test_serviceAdd()