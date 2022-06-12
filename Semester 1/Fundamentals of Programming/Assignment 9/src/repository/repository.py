from src.domain.book import Book
from src.domain.client import Client
from src.domain.rentals import Rental
from src.errors.repoErrors import RepoError
from src.repository.module import Module
from datetime import date
import pickle
import json



class Repo:
    def __init__(self):
        self._data = Module()

    def add(self, entity): #tested
        if entity.ID in self._data():
            raise RepoError(f'Entity(ID: {entity.ID}) is already in repo.')
        self._data[entity.ID] = entity

    def __call__(self): #tested
        return self._data()

    def sort(self, list, cmpFunction):
        return self._data.sort(list, cmpFunction)

    def filter(self, list, cmpFunction):
        return self._data.filter(list, cmpFunction)

    def __len__(self): #tested
        return len(self._data)

    def __getitem__(self, item): #tested
        if item not in self._data():
            raise RepoError(f'The entity with ID: {item} is not in repo.')

        return self._data[item]

    def __setitem__(self, key, value): #tested
        if key not in self._data():
            raise RepoError(f'The entity with ID: {key} is not in repo.')

        self._data[key] = value

    def __delitem__(self, key):
        if key not in self._data():
            raise RepoError(f'The entity with ID: {key} is not in repo.')

        del self._data[key]

    def getList(self): #tested
        return self._data().values()


"""
MySQL BASED REPOSITORY
"""

"""
BINARY FILES BASED REPOSITORY
"""

class PickleRepo(Repo):
    def __init__(self, fileName):
        super().__init__()

        self._fileName = fileName
        self._loadFile()

    def _loadFile(self):
        f = open(self._fileName, "rb")
        self._data = pickle.load(f)

        f.close()

    def _saveFile(self):
        f = open(self._fileName, "wb")
        pickle.dump(self._data, f)
        f.close()

    def add(self, entity):
        super(PickleRepo, self).add(entity)

        self._saveFile()

"""
JSON BASED REPOSITORY
"""


def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, date):
        format = "%Y-%m-%d"
        serial = obj.strftime(format)
        return serial

    return obj.__dict__

class BookJSONRepo(Repo):
    def __init__(self, fileName):
        super().__init__()

        self._fileName = fileName
        self._loadFile()

    def _loadFile(self):
        f = open(self._fileName, "rt")
        dict = json.load(f)
        for item in dict:
            items = dict[item]
            self.add(Book(items["_Book__bookID"], items["_Book__author"], items["_Book__title"], items["_Book__isAvailable"],
                          items["_Book__rentNumber"]))
        f.close()

    def _saveFile(self):
        f = open(self._fileName, "wt")
        json.dump(self._data, f, indent=2, default= lambda x: serialize(x))
        f.close()

    def add(self, entity):
        super(BookJSONRepo, self).add(entity)

        self._saveFile()

class ClientJSONRepo(Repo):
    def __init__(self, fileName):
        super().__init__()

        self._fileName = fileName
        self._loadFile()

    def _loadFile(self):
        f = open(self._fileName, "rt")
        dict = json.load(f)
        for item in dict:
            items = dict[item]
            self.add(Client(items["_Client__clientID"], items["_Client__name"], items["_Client__activeRental"],
                          items["_Client__daysRented"]))
        f.close()

    def _saveFile(self):
        f = open(self._fileName, "wt")
        json.dump(self._data, f, indent=2, default= lambda x: serialize(x))
        f.close()

    def add(self, entity):
        super(ClientJSONRepo, self).add(entity)

        self._saveFile()

class RentalJSONRepo(Repo):
    def __init__(self, fileName):
        super().__init__()

        self._fileName = fileName
        self._loadFile()

    def _loadFile(self):
        f = open(self._fileName, "rt")
        dict = json.load(f)
        for item in dict:
            items = dict[item]
            self.add(Rental(items["_Rental__rentID"], items["_Rental__client"], items["_Rental__book"],
                            date.fromisoformat(items["_Rental__rentDate"]), date.fromisoformat(items["_Rental__returnDate"])))
        f.close()

    def _saveFile(self):
        f = open(self._fileName, "wt")
        json.dump(self._data, f, indent=2, default= lambda x: serialize(x))
        f.close()

    def add(self, entity):
        super(RentalJSONRepo, self).add(entity)

        self._saveFile()
"""
FILE BASED REPOSITORY
"""

class BookFileRepo(Repo):
    def __init__(self, filename):
        super().__init__()

        self._fileName = filename
        self._loadFile()

    def _loadFile(self):
        f = open(self._fileName, "rt")
        for line in f.readlines():
            _id, author, title, isAvailable, rentNumber = line.split(sep=',')
            self.add(Book(int(_id.strip()), author.strip(), title.strip(), bool(int(isAvailable.strip())), int(rentNumber.strip())))
        f.close()

    def _saveFile(self):
        f = open(self._fileName, "wt")
        for book in self.getList():
            f.write(f"{book.ID}, {book.author}, {book.title}, {int(book.getAvailability())}, {book.getRentNumber()}\n")

        f.close()

    def add(self, entity):
        super(BookFileRepo, self).add(entity)

        self._saveFile()

class ClientFileRepo(Repo):
    def __init__(self, filename):
        super().__init__()

        self._fileName = filename
        self._loadFile()

    def _loadFile(self):
        f = open(self._fileName, "rt")
        for line in f.readlines():
            _id, name, activeRental, daysRented = line.split(sep=',')
            self.add(Client(int(_id.strip()), name.strip(), bool(int(activeRental.strip())), int(daysRented.strip())))
        f.close()

    def _saveFile(self):
        f = open(self._fileName, "wt")
        for client in self.getList():
            f.write(f"{client.ID}, {client.name}, {int(client.activeRental())}, {client.getDaysRented()}\n")

        f.close()

    def add(self, entity):
        super(ClientFileRepo, self).add(entity)

        self._saveFile()

class RentalFileRepo(Repo):
    def __init__(self, filename):
        super().__init__()

        self._fileName = filename
        self._loadFile()

    def _loadFile(self):
        f = open(self._fileName, "rt")
        for line in f.readlines():
            _id, client, book, rent, unrent = line.split(sep=',')

            rentDate = date.fromisoformat(rent.strip())
            unrentDate = date.fromisoformat(unrent.strip())

            self.add(Rental(int(_id.strip()), int(book.strip()), int(client.strip()), rentDate, unrentDate))
        f.close()

    def _saveFile(self):
        f = open(self._fileName, "wt")
        format = "%Y-%m-%d"
        for rental in self.getList():
            f.write(f"{rental.ID}, {rental.client}, {rental.book}, {rental.rent.strftime(format)}, {rental.unrent.strftime(format)}\n")

        f.close()

    def add(self, entity):
        super(RentalFileRepo, self).add(entity)

        self._saveFile()