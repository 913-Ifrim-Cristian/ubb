from texttable import Texttable

from src.errors.errors import BoardError

class Board:
    def __init__(self, difficulty):
        self._difficulty = difficulty
        self._size = 2 * difficulty + 8
        self._data = [[' '] * self._size for i in range(self._size)]
        self._number_of_planes = difficulty + 3
        self._planes = {}

        if difficulty == 3:
            self._number_of_planes = 8

    @property
    def difficulty(self):
        # Getter function for difficulty
        return self._difficulty

    @property
    def size(self):
        # Getter function for size
        return self._size

    @property
    def data(self):
        # Getter function for data
        return self._data

    @property
    def planes(self):
        # Getter function for planes dictionary
        return self._planes

    @property
    def number_of_planes(self):
        # Getter function for number_of_planes although i dont use this
        return self._number_of_planes

    def get_hit(self, x, y):
        """
        This function registers if a given input coordinates are crashes, hits or nothings and also marks the hit spot with X
        :param x:
        :param y:
        :return:
        """
        if (x, y) in self._planes:
            for item in self._planes[(x, y)]:
                self._data[x][y] = 'X'
                self._data[item[0]][item[1]] = 'X'
            return 1
        for item in self._planes:
            if (x, y) in self._planes[item]:
                self._data[x][y] = 'X'
                return 0
        self._data[x][y] = 'X'
        return -1

    def validate_positions(self, x, y, orientation):
        """
        This function validates a certain tuple (x, y) so it can be used as coordinates for a planes cabin
        :param x:
        :param y:
        :param orientation:
        :return:
        """
        if x < 0 or x >= self._size or y < 0 or y >= self._size:
            raise BoardError("Coordinates are outside the board!")
        if self._data[x][y] != ' ':
            raise BoardError("Planes must not overlap!")
        if orientation == 'N':
            for i in range(1, 4):
                if x + i >= self._size:
                    raise BoardError("Planes must not overlap the board!")
                if self._data[x + i][y] != ' ':
                    raise BoardError("Planes must not overlap!")
            n = 2
            if self._difficulty > 1:
                n = 3
                if self._data[x + 1][y + 2] != ' ':
                    raise BoardError("Planes must not overlap!")
                if self._data[x + 1][y - 2] != ' ':
                    raise BoardError("Planes must not overlap!")

            for i in range(1, n):
                if y + i >= self._size:
                    raise BoardError("Planes must not overlap the board!")
                if y - i < 0:
                    raise BoardError("Planes must not overlap the board!")

            if self._data[x + 1][y + 1] != ' ':
                raise BoardError("Planes must not overlap!")
            if self._data[x + 1][y - 1] != ' ':
                raise BoardError("Planes must not overlap!")
            if self._data[x + 3][y + 1] != ' ':
                raise BoardError("Planes must not overlap!")
            if self._data[x + 3][y - 1] != ' ':
                raise BoardError("Planes must not overlap!")
        elif orientation == 'S':
            for i in range(1, 4):
                if x - i < 0:
                    raise BoardError("Planes must not overlap the board!")
                if self._data[x - i][y] != ' ':
                    raise BoardError("Planes must not overlap!")
            n = 2
            if self._difficulty > 1:
                n = 3
                if self._data[x - 1][y + 2] != ' ':
                    raise BoardError("Planes must not overlap!")
                if self._data[x - 1][y - 2] != ' ':
                    raise BoardError("Planes must not overlap!")

            for i in range(1, n):
                if y + i >= self._size:
                    raise BoardError("Planes must not overlap the board!")
                if y - i < 0:
                    raise BoardError("Planes must not overlap the board!")

            if self._data[x - 1][y + 1] != ' ':
                raise BoardError("Planes must not overlap!")
            if self._data[x - 1][y - 1] != ' ':
                raise BoardError("Planes must not overlap!")
            if self._data[x - 3][y + 1] != ' ':
                raise BoardError("Planes must not overlap!")
            if self._data[x - 3][y - 1] != ' ':
                raise BoardError("Planes must not overlap!")

        elif orientation == 'E':
            for i in range(1, 4):
                if y - i < 0:
                    raise BoardError("Planes must not overlap the board!")
                if self._data[x][y - i] != ' ':
                    raise BoardError("Planes must not overlap!")
            n = 2
            if self._difficulty > 1:
                n = 3
                if self._data[x + 2][y - 1] != ' ':
                    raise BoardError("Planes must not overlap!")
                if self._data[x - 2][y - 1] != ' ':
                    raise BoardError("Planes must not overlap!")

            for i in range(1, n):
                if x + i >= self._size:
                    raise BoardError("Planes must not overlap the board!")
                if x - i < 0:
                    raise BoardError("Planes must not overlap the board!")

            if self._data[x + 1][y - 1] != ' ':
                raise BoardError("Planes must not overlap!")
            if self._data[x - 1][y - 1] != ' ':
                raise BoardError("Planes must not overlap!")
            if self._data[x + 1][y - 3] != ' ':
                raise BoardError("Planes must not overlap!")
            if self._data[x - 1][y - 3] != ' ':
                raise BoardError("Planes must not overlap!")

            elif orientation == 'W':
                for i in range(1, 4):
                    if y + i >= self._size:
                        raise BoardError("Planes must not overlap the board!")
                    if self._data[x][y + i] != ' ':
                        raise BoardError("Planes must not overlap!")
                n = 2
                if self._difficulty > 1:
                    n = 3
                    if self._data[x + 2][y + 1] != ' ':
                        raise BoardError("Planes must not overlap!")
                    if self._data[x - 2][y + 1] != ' ':
                        raise BoardError("Planes must not overlap!")

                for i in range(1, n):
                    if x + i >= self._size:
                        raise BoardError("Planes must not overlap the board!")
                    if x - i < 0:
                        raise BoardError("Planes must not overlap the board!")

                if self._data[x + 1][y + 1] != ' ':
                    raise BoardError("Planes must not overlap!")
                if self._data[x - 1][y + 1] != ' ':
                    raise BoardError("Planes must not overlap!")
                if self._data[x + 1][y + 3] != ' ':
                    raise BoardError("Planes must not overlap!")
                if self._data[x - 1][y + 3] != ' ':
                    raise BoardError("Planes must not overlap!")


    def add_plane(self, x, y, orientation):
        """
        This function adds a plane at a given position (x, y) with a specific orientation, all validations are done in service class
        :param x:
        :param y:
        :param orientation:
        :return:
        """

        if orientation == "N":

            self._planes[(x, y)] = []
            self._planes[(x, y)].append((x + 1, y))
            self._planes[(x, y)].append((x + 1, y + 1))
            self._planes[(x, y)].append((x + 1, y - 1))

            if self._difficulty > 1:
                self._planes[(x, y)].append((x + 1, y + 2))
                self._planes[(x, y)].append((x + 1, y - 2))

            self._planes[(x, y)].append((x + 2, y))
            self._planes[(x, y)].append((x + 3, y))
            self._planes[(x, y)].append((x + 3, y + 1))
            self._planes[(x, y)].append((x + 3, y - 1))

        elif orientation == "S":

            self._planes[(x, y)] = []
            self._planes[(x, y)].append((x - 1, y))
            self._planes[(x, y)].append((x - 1, y + 1))
            self._planes[(x, y)].append((x - 1, y - 1))

            if self._difficulty > 1:
                self._planes[(x, y)].append((x - 1, y + 2))
                self._planes[(x, y)].append((x - 1, y - 2))

            self._planes[(x, y)].append((x - 2, y))
            self._planes[(x, y)].append((x - 3, y))
            self._planes[(x, y)].append((x - 3, y + 1))
            self._planes[(x, y)].append((x - 3, y - 1))

        elif orientation == "W":

            self._planes[(x, y)] = []
            self._planes[(x, y)].append((x, y + 1))
            self._planes[(x, y)].append((x + 1, y + 1))
            self._planes[(x, y)].append((x - 1, y + 1))

            if self._difficulty > 1:
                self._planes[(x, y)].append((x + 2, y + 1))
                self._planes[(x, y)].append((x - 2, y + 1))

            self._planes[(x, y)].append((x, y + 2))
            self._planes[(x, y)].append((x, y + 3))
            self._planes[(x, y)].append((x + 1, y + 3))
            self._planes[(x, y)].append((x - 1, y + 3))

        elif orientation == "E":

            self._planes[(x, y)] = []
            self._planes[(x, y)].append((x, y - 1))
            self._planes[(x, y)].append((x + 1, y - 1))
            self._planes[(x, y)].append((x - 1, y - 1))

            if self._difficulty > 1:
                self._planes[(x, y)].append((x + 2, y - 1))
                self._planes[(x, y)].append((x - 2, y - 1))

            self._planes[(x, y)].append((x, y - 2))
            self._planes[(x, y)].append((x, y - 3))
            self._planes[(x, y)].append((x + 1, y - 3))
            self._planes[(x, y)].append((x - 1, y - 3))

    def __str__(self):
        """
        This function returns the table in which are the planes represented
        :return:
        """

        t = Texttable()

        table_header = ['/']

        for i in range(self._size):
            table_header.append(i+1)

        t.header(table_header)

        for i in range(self._size):
            table_row = [chr(65+i)]

            for j in range(self._size):
                table_row.append(self._data[i][j])

            t.add_row(table_row)

        return t.draw()


class ComputerBoard(Board):

    """
    Had some plans with it but were worthless
    """

    def __init__(self, difficulty):
        super().__init__(difficulty)


class PlayerBoard(Board):

    """
    PlayerBoard class, which overloads add_plane in order to show the planes for the player
    """

    def __init__(self, difficulty):
        super().__init__(difficulty)

    def add_plane(self, x, y, orientation):
        super().add_plane(x, y, orientation)
        for item in self._planes:
            self._data[item[0]][item[1]] = 'C'
            for itm in self._planes[item]:
                x, y = itm[0], itm[1]
                self._data[x][y] = 'A'


