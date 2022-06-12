class Book:
    """
    This is the domain class of the program in which is represented a book
    """
    _booksNumber = 0 # the counter of how many instances are created
    _isbnList = [] # the isbn list to check if the isbn added is unique
    def __init__(self, isbn, author = "Anonymous", title = "Untitled"):
        """
        This is the constructor of the class and assigns the values given as parameters + does some checkings
        :param isbn:
        :param author:
        :param title:
        """
        if isbn in Book._isbnList:
            raise ValueError("Couldn't add this book as it is already added")
        self.__isbn = isbn
        if author == "":
            author = "Anonymous"
        self.__author = author
        if title == "":
            title = "Untitled"
        self.__title = title

        Book._booksNumber += 1
        Book._isbnList.append(isbn)

    @property
    def isbn(self): #isbn() -> getter
        """
        Getter function of isbn
        :return:
        """
        return self.__isbn

    @isbn.setter
    def isbn(self, value): #isbn(50) -> setter
        """
        Setter function of isbn
        :param value:
        :return:
        """
        self.__isbn = value

    @property
    def author(self):
        """
        Getter function of author
        :return:
        """
        return self.__author

    @author.setter
    def author(self, value):
        """
        Setter function for author
        :param value:
        :return:
        """
        self.__author = value

    @property
    def title(self):
        """
        Getter instance for title variable
        :return:
        """
        return self.__title

    @title.setter
    def title(self, value):
        """
        Setter instace for title variable
        :param value:
        :return:
        """
        self.__title = value

    @staticmethod
    def getInstances():
        """
        A method for class Book that returns the number of created Books
        :return:
        """
        return Book._booksNumber

    def __str__(self):
        """
        str() function overloader to format the book
        :return:
        """
        s = "ISBN: " + self.isbn + ", Author: " + self.author + ", Title: " + self.title
        return s

    def getFirstWord(self):
        """
        Getter function for the first word of the title # -> used in filter function
        :return:
        """
        return self.__title.split()[0].lower()