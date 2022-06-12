from src.errors.errors import ServiceError

class PlayerService:
    def __init__(self, player_board):
        self.__player_board = player_board

    @property
    def board(self):
        #getter function for the board class
        return self.__player_board

    def add_plane(self, x, y, orientation):
        """
        This function adds a plane into the board and validates the coordinates
        :param x:
        :param y:
        :param orientation:
        :return:
        """
        if orientation.upper() not in ['N', 'S', 'E', 'W']:
            raise ServiceError("Wrong orientation!")

        self.__player_board.validate_positions(x, y, orientation)
        self.__player_board.add_plane(x, y, orientation)

    def get_hit(self, x, y):
        """
        This function registers if a given input coordinates are crashes, hits or nothings and also marks the hit spot with X
        :param x:
        :param y:
        :return:
        """
        return self.__player_board.get_hit(x, y)

