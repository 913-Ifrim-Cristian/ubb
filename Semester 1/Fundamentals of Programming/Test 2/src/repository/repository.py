class RepoError(Exception):

    def __init__(self, message = "Repository Error! Please be careful with input data."):
        self.__message = message
        super().__init__(self.__message)

class Repo:
    def __init__(self):
        self.__data = dict()

    def _checkDistance(self, taxi):
        for item in self.__data:
            if abs(self.__data[item].x - taxi.x) + abs(self.__data[item].y - taxi.y) < 6:
                return False
        return True

    def add(self, entity):
        if entity.ID in self.__data:
            raise RepoError(f'Entity(ID: {entity.ID}) is already in repo.')
        if self._checkDistance(entity) is False:
            raise RepoError(f'Entity(ID: {entity.ID}) is too close to another entity')

        self.__data[entity.ID] = entity

    def __call__(self):
        return self.__data

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, item):
        if item not in self.__data:
            raise RepoError(f'The entity with ID: {item} is not in repo.')

        return self.__data[item]

    def __setitem__(self, key, value):
        if key not in self.__data:
            raise RepoError(f'The entity with ID: {key} is not in repo.')

        self.__data[key] = value

    def __delitem__(self, key):
        if key not in self.__data:
            raise RepoError(f'The entity with ID: {key} is not in repo.')

        del self.__data[key]

    def getList(self):
        return self.__data.values()


