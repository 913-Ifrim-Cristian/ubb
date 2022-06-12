from src.errors.errors import ServiceError
from random import randint

class ComputerService:
    def __init__(self, board, validator):
        """
        Constructor for computer service
        :param board:
        :param validator:
        """
        self.__board = board
        self.__validator = validator
        self.__pieces = {}

    def load_data(self):
        """
        Loads the pieces from the file
        :return:
        """
        l = self.__board.return_computer_pieces()
        for item in l:
            self.__pieces[item] = 'O'

    def move(self):
        """
        Moves a piece from a position to another
        :return:
        """
        ok = 1
        while ok == 1:
            x, y = randint(0, 2), randint(0, 2)
            i, j = randint(0, 2), randint(0, 2)
            if (i, j) not in self.__pieces:
                continue
            if self.__board.is_occupied(x, y) is True:
                continue
            if self.__validator.valid_move(x, y, i, j) is True:
                self.__board.move('O', i, j, x, y)
                del self.__pieces[(i, j)]
                self.__pieces[(x, y)] = 'O'
                ok = 0

    def placement(self):
        """
        Places a piece
        :return:
        """
        ok = 1
        while ok == 1:
            x, y = randint(0, 2), randint(0, 2)
            if self.__board.is_occupied(x, y) is True:
                continue
            self.__board.place('O', x, y)
            self.__pieces[(x, y)] = 'O'
            ok = 0


    def check_win(self):
        """
        Checks if computer won
        :return:
        """
        # Diagonal check
        counter = 0
        for i in range(3):
            if (i, i) in self.__pieces:
                counter += 1
                if counter == 3:
                    return True
        counter = 0
        # 2nd diagonal check
        for i in range(3):
            for j in range(3):
                if i + j == 3:
                    if (i, j) in self.__pieces:
                        counter += 1
                        if counter == 3:
                            return True
        # row check
        for i in range(3):
            counter = 0
            for j in range(3):
                if (i, j) in self.__pieces:
                    counter += 1
                    if counter == 3:
                        return True
        # column check
        for i in range(3):
            counter = 0
            for j in range(3):
                if (j, i) in self.__pieces:
                    counter += 1
                    if counter == 3:
                        return True
        return False