from src.domain.book import Book
from src.domain.client import Client
from src.errors.repoErrors import RepoError


class Repo:
    def __init__(self):
        self.__data = dict()

    def add(self, entity): #tested
        if entity.ID in self.__data:
            raise RepoError(f'Entity(ID: {entity.ID}) is already in repo.')
        self.__data[entity.ID] = entity

    def __call__(self): #tested
        return self.__data

    def __len__(self): #tested
        return len(self.__data)

    def __getitem__(self, item): #tested
        if item not in self.__data:
            raise RepoError(f'The entity with ID: {item} is not in repo.')

        return self.__data[item]

    def __setitem__(self, key, value): #tested
        if key not in self.__data:
            raise RepoError(f'The entity with ID: {key} is not in repo.')

        self.__data[key] = value

    def __delitem__(self, key):
        if key not in self.__data:
            raise RepoError(f'The entity with ID: {key} is not in repo.')

        del self.__data[key]

    def getList(self): #tested
        return self.__data.values()

