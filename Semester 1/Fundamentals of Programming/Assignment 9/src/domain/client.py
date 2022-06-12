class Client:
    def __init__(self, id, name, activeRental = False, daysRented = 0):
        self.__clientID = id
        self.__name = name
        self.__activeRental = activeRental
        self.__daysRented = daysRented

    @property
    def ID(self):
        return self.__clientID

    @ID.setter
    def ID(self, id):
        self.__clientID = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def activeRental(self):
        return self.__activeRental

    def toggleActiveRental(self):
        self.__activeRental = not self.__activeRental

    def addDaysRented(self, days):
            self.__daysRented += days

    def getDaysRented(self):
        return self.__daysRented

    def __gt__(self, other):
        return self.__daysRented > other.getDaysRented()

    def __lt__(self, other):
        return self.__daysRented < other.getDaysRented()

    def __eq__(self, other):
        return self.__clientID == other.ID and\
               self.__name == other.name and\
               self.__daysRented == other.getDaysRented() and\
               self.__activeRental == other.activeRental()

    def __str__(self):
        return f'Client ID: {self.__clientID}, Name: {self.__name}, Rent Days: {self.__daysRented}, Active Rent: {self.__activeRental}'