from texttable import Texttable

class Board:
    def __init__(self, filename):
        """
        Constructor class for board
        :param filename:
        """
        self.__data = [[' ', ' ', ' '] for x in range(3)]
        self.__file_name = filename

    def save_data(self):
        """
        Saves the data to file
        :return:
        """
        f = open(self.__file_name, "wt")
        for item in range(3):
            for items in range(3):
                f.write(str(self.__data[item][items]) + ',')
        f.close()

    def return_player_pieces(self):
        """
        Returns the player pieces from data, used in continuing game
        :return:
        """
        l = []
        for item in range(3):
            for items in range(3):
                if self.__data[item][items] == 'X':
                    l.append((item, items))
        return l
    def return_computer_pieces(self):
        """
        Returns the computer pieces from data, used in continuing game
        :return:
        """
        l = []
        for item in range(3):
            for items in range(3):
                if self.__data[item][items] == 'O':
                    l.append((item, items))
        return l

    def load_data(self):
        """
        Loads the data from the file
        :return:
        """
        f = open(self.__file_name, "rt")
        counter = 0
        for line in f.readlines():
            x = line.split(',')

            for i in range(len(x)-1):
                self.__data[counter][i % 3] = x[i]
                if i % 3 == 2:
                    counter += 1

    def place(self, owner, i, j):
        """
        Places a piece on the board
        :param owner:
        :param i:
        :param j:
        :return:
        """
        self.__data[i][j] = owner
        self.save_data()


    def move(self, owner, i, j, x, y):
        """
        Moves a piece on the board
        :param owner:
        :param i:
        :param j:
        :param x:
        :param y:
        :return:
        """
        self.__data[i][j] = ' '
        self.__data[x][y] = owner
        self.save_data()

    def is_occupied(self, i, j):
        """
        Checks if a slot on board is occupied
        :param i:
        :param j:
        :return:
        """
        if self.__data[i][j] != ' ':
            return True
        return False

    def __str__(self):
        """
        Returns the table in a pretty format :)
        :return:
        """
        t = Texttable()
        for i in range(3):
            l = []
            for j in range(3):
                l.append(self.__data[i][j])
            t.add_row(l)

        return t.draw()