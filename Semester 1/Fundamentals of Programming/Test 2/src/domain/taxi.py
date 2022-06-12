class Taxi:
    def __init__(self, id, x, y):
        self.__id = id
        self.__x = x
        self.__y = y
        self.__fare = 0

    @property
    def ID(self):
        return self.__id
    @ID.setter
    def ID(self, value):
        self.__id = value

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def fare(self):
        return self.__fare
    @fare.setter
    def fare(self, value):
        self.__fare = value

    def __lt__(self, other):
        return self.__fare < other.fare

    def __gt__(self, other):
        return self.__fare > other.fare

    def __str__(self):
        return f"Taxi ID: {self.__id}, Location: ({self.__x}, {self.__y}), Fare: {self.__fare}"
