from src.errors.repoErrors import RepoError
from src.errors.serviceErrors import ServiceError
from src.domain.client import Client
from src.services.generators import authorGenerator
from src.services.validators import ClientValidator

"""
Client service module
This module works only with clients functionalities and does not interfere with books functions
There we will update the state of a client or rental:
    -Add, remove, update clients fields(ID, name)
    -Rent a book, return a book
    -Search for a client by fields
    -Statistics: Most active clients
"""

class ClientService:
    def __init__(self, repo, validator, generator):
        """
        The constructor of the client service class and also generates 25 random values
        :param repo:
        :param validator:
        """
        self.__repo = repo
        self.__validator = validator

        if generator is True:
            idx = 0
            while (idx < 10):
                self.__repo.add(Client(idx, authorGenerator()))
                idx += 1

    def __call__(self): #tested
        """
        This function calls the repo dictionary
        :return:
        """
        return self.__repo()

    def __getitem__(self, item): #tested
        """
        Getter for the repo[item] from repo dict
        :param item:
        :return:
        """
        return self.__repo[item]

    def __delitem__(self, key): #tested
        """
        Deletes the repo[key] item from the list
        :param key:
        :return:
        """
        del self.__repo[key]

    def addClient(self, cID, cName, activeRental = False, rentDays = 0): #tested
        """
        Add a client to the repo
        1. Create a new client
        2. Validate data
        3. Add to repo
        :param cID: the id of the client
        :param cName: the name of the client
        :return: --
        """

        client = Client(cID, cName, activeRental, rentDays)  # 1
        self.__validator.validateClient(client)  # 2
        self.__repo.add(client)  # 3

    def searchClientByID(self, bID): #tested
        """
        Searches a client by its ID in the repo
        :param bID:
        :return:
        """
        if bID not in self.__repo():
            raise RepoError(f'The entity with ID: {bID} is not in repo.')

        return self.__repo[bID]

    def searchClientByName(self, bTitle): #tested
        l = []
        for item in self.__repo():
            if bTitle.lower() in self.__repo[item].name.lower():
                l.append(self.__repo[item])

        if len(l) == 0:
            raise ServiceError(f"No client that has it's name containing {bTitle} was found.")
        return l


    def updateClient(self, cID, cName): #tested
        """
        Updates the name of the client
        :param cID:
        :param cName:
        :return:
        """
        if cID not in self.__repo():
            raise RepoError(f'The entity with ID: {cID} is not in repo.')

        self.__repo[cID].name = cName

    def mostActiveClients(self): #tested
        """
        Statistics for the most rented books
        :return:
        """
        clients = list(self.__repo.getList())
        clients.sort(reverse=True)

        return clients
