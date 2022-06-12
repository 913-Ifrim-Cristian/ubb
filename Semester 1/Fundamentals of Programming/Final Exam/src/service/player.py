from src.errors.errors import ServiceError
class PlayerService:
    """
    Constructor class for player service
    """
    def __init__(self, board, validator):
        self.__pieces = {}
        self.__validator = validator
        self.__board = board

    @property
    def board(self):
        """
        Board getter
        :return:
        """
        return self.__board

    def load_data(self):
        """
        Loads the pieces from the file
        :return:
        """
        l = self.__board.return_player_pieces()
        for item in l:
            self.__pieces[item] = 'X'

    def move(self, i, j, x, y):
        """
        Validates and moves a piece
        :param i:
        :param j:
        :param x:
        :param y:
        :return:
        """
        if (i, j) not in self.__pieces:
            raise ServiceError("Invalid piece!")
        if self.__board.is_occupied(x, y):
            raise ServiceError("Invalid move. Position is occupied!")
        if self.__validator.valid_move(x, y, i, j) is False:
            raise ServiceError("Invalid move!")
        self.__pieces[(x, y)] = 'X'
        del self.__pieces[(i, j)]
        self.__board.move('X', i, j, x, y)


    def place(self, i, j):
        """
        Places a piece
        :param i:
        :param j:
        :return:
        """
        if self.__validator.valid_placement(i, j) is False:
            raise ServiceError("Invalid placement!")
        if self.__board.is_occupied(i, j) is True:
            raise ServiceError("Invalid move. Position is occupied")

        self.__pieces[(i, j)] = 'X'
        self.__board.place('X', i, j)

    def number_of_pieces(self):
        """
        Getter for the number of pieces placed
        :return:
        """
        return len(self.__pieces)

    def check_win(self):
        """
        Checks if player wins
        :return:
        """
        #Diagonal check
        counter = 0
        for i in range(3):
            if (i, i) in self.__pieces:
                counter += 1
                if counter == 3:
                    return True
        counter = 0
        #2nd diagonal check
        for i in range(3):
            for j in range(3):
                if i + j == 3:
                    if (i, j) in self.__pieces:
                        counter += 1
                        if counter == 3:
                            return True
        #row check
        for i in range(3):
            counter = 0
            for j in range(3):
                if (i, j) in self.__pieces:
                    counter += 1
                    if counter == 3:
                        return True
        #column check
        for i in range(3):
            counter = 0
            for j in range(3):
                if (j, i) in self.__pieces:
                    counter += 1
                    if counter == 3:
                        return True
        return False