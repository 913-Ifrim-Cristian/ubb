import random
from src.domain.domain import Book

class Service:
    """
    This class is a service class that contains all the functionalities that does not require user input or any output
    """
    def __init__(self):
        """
        The constructor of the class which creates the lists needed and generates 10 values
        """
        self._booksHistory = []
        self._booksList = []
        for i in range(0, 10):
            x = Book(isbnGenerator(), authorGenerator(), titleGenerator())
            self._booksList.append(x)

    def add(self, book):
        """
        This command implements the add a book feature
        Firstly checks if the input data is correct and then adds the book to the list
        :param book:
        :return:
        """
        if checkISBN(book.isbn) is False:
            raise ValueError("Incorrect ISBN format! Please use 3-1-4-4-1 format!\n")
        if hasDigits(book.author) is True:
            raise ValueError("Incorrect name! A name cannot contain digits!\n")
        if hasDigits(book.title) is True:
            raise ValueError("Incorrect title! A title cannot contain digits!\n")

        newList = self._booksList[:]
        self._booksHistory.append(newList)
        self._booksList.append(book)

    def getList(self):
        """
        Getter function for the list of books -> used for tests xd
        :return:
        """
        return self._booksList

    def undo(self):
        """
        Basic undo functionality that restores the last list from a backup list :D
        :return:
        """
        if len(self._booksHistory) == 0:
            raise ValueError("Cannot undo! There are no operations left.\n")
        self._booksList = self._booksHistory.pop()[:]

    def filter(self, word):
        """
        This function implements the filter functionality.
        First it checks if there are any titles that begin with the given word and then filters the list
        :param word:
        :return:
        """
        found = 0
        for item in self._booksList:
            if item.getFirstWord() == word:
                found = 1
                break
        if found == 0:
            raise ValueError("Cannot filter! There are no titles that begin with word " + word + "!\n")

        newList = self._booksList[:]
        self._booksHistory.append(newList)

        for item in range(len(self._booksList)-1, -1, -1):
            if self._booksList[item].getFirstWord() == word:
                self._booksList.pop(item)

#isbn generator 3-1-4-4-1
def isbnGenerator():
    """
    A random-isbn generator to create a random book
    :return:
    """
    s = ""
    nr = random.randint(100, 1000)
    s += str(nr) + "-"
    nr = random.randint(1, 10)
    s += str(nr)+ "-"
    nr = random.randint(1000, 10000)
    s += str(nr) + "-"
    nr = random.randint(1000, 10000)
    s += str(nr) + "-"
    nr = random.randint(1, 10)
    s += str(nr)
    return s

def hasDigits(string):
    """
    This function checks if a string contains digits -> used for checking title and author validity
    :param string:
    :return:
    """
    return any(i.isdigit() for i in string)

def checkISBN(isbn):
    """
    This function checks if the isbn respects de 3-1-4-4-1 format
    :param isbn:
    :return:
    """
    if len(isbn) != 17:
        return False
    isbnTokens = isbn.split('-')

    if len(isbnTokens[0]) != 3:
        return False
    if len(isbnTokens[1]) != 1:
        return False
    if len(isbnTokens[2]) != 4:
        return False
    if len(isbnTokens[3]) != 4:
        return False
    if len(isbnTokens[4]) != 1:
        return False
    for item in isbnTokens:
        if not item.isdigit():
            return False

    return True

#author generator
def authorGenerator():
    """
    This function generates author names randomly
    :return:
    """
    secondName = ['Gheorghidiu', 'Iancu', 'Glanetasu', 'Muller', 'Miller', 'Seagal', 'Catana', 'Avram', 'Statham', 'Bravo', 'Usher', 'Hammond', 'Carlson', 'Dicky', 'Matthew', 'Williamson', 'Creanga', 'Rebreanu', 'Vijelie', 'Pinkman', 'Shelby', 'Escobar', 'Lothbrok', 'Ironside', 'Guzman']
    firstName = ['Aurelian', 'Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 'Mason', 'Michael', 'Ethan', 'Daniel', 'Jacob', 'Logan', 'Jackson', 'Levi', 'Sebastian', 'Mateo', 'Jack', 'Owen', 'Theodore', 'Aiden', 'Samuel', 'Joseph', 'John', 'David', 'Wyatt', 'Matthew', 'Luke', 'Asher', 'Carter', 'Julian', 'Grayson', 'Leo', 'Jayden', 'Gabriel', 'Isaac', 'Lincoln', 'Anthony', 'Hudson', 'Dylan', 'Ezra', 'Thomas', 'Charles', 'Christopher', 'Jaxon', 'Maverick', 'Josiah', 'Isaiah', 'Andrew', 'Elias', 'Joshua', 'Nathan', 'Caleb', 'Ryan', 'Adrian', 'Miles', 'Eli', 'Nolan', 'Christian', 'Aaron', 'Cameron', 'Ezekiel', 'Colton', 'Luca', 'Landon', 'Hunter', 'Jonathan', 'Santiago', 'Axel', 'Easton', 'Cooper', 'Jeremiah', 'Angel', 'Roman']

    s = firstName[random.randint(0, len(firstName)-1)] + " " + secondName[random.randint(0, len(secondName)-1)]
    return s

def titleGenerator():
    """
    This function returns titles of books randomly
    :return:
    """
    titles = ["Valentine In My Town", "Boy In The Mountain", "Visitors Without Time", "Valentines Of The Stars",
     "Foreigners And Assistants", "Men And Suitors", "Kiss Of My Fascination", "Determination Of Bliss",
     "Songs Of The Wife", "Calling My Nightmares", "Secret Admirer Of The West", "Foreigner Of Hope", "Men Of Bliss",
     "Men Of Romance", "Roommates And Honeys", "Guests And Neighbors", "Rise Of Rainbows", "Origin Of The Ocean",
     "Chasing My Sweetheart", "Sounds Of The Shadows", "Friend Without Shame", "Dearest Of The Mountains",
     "Girls With Black Hair", "Secret Admirers Of Paradise", "Wifes And Angels", "Beloved And Foreigners",
     "Scent Of My Dreams", "Disruption In The River", "Admiring Lust", "Songs Of My Girl", "Boy In The Hallway",
     "Raven Project", "Knight Makeover", "Thief Prophecy", "Soldier And Girl", "Fool And Woman",
     "Parody Of The Country", "Trouble Has Been Naughty", "Trust That Idiot", "Love Of The Device",
     "Descendant Of Last Rites", "Thief Of Gold", "Horses Of The Forsaken", "Guardians Of The Nation",
     "Bringers And Collectors", "Scientists And Boys", "Border Of Glory", "Vengeance Of The Stars",
     "Avoiding The Mountains", "Altering The Shadows"]

    return titles[random.randint(0, len(titles)-1)]