from random import randint

data_set_easy = [['A3N', 'A7N', 'G4E'], ['B3W', 'G3S', 'H6S'], ['A3N', 'D5W', 'E4N'],
                 ['B5W', 'D5E', 'G4E'], ['D3S', 'D4E', 'F1E'], ['F1W', 'E8E', 'B4W']]

data_set_normal = [['A3N', 'B5N', 'G9S', 'I3W'], ['A3N', 'B5N', 'G9S', 'I3W'], ['A3N', 'B5N', 'G9S', 'I3W'],
                   ['A3N', 'B5N', 'G9S', 'I3W'], ['A3N', 'B5N', 'G9S', 'I3W'], ['A3N', 'B5N', 'G9S', 'I3W']]

data_set_hard = [['C3W', 'E6N', 'J2W', 'J10E', 'H10S'], ['G4E', 'L6S', 'I10N', 'C8E', 'A10N'],
                 ['E5E', 'G10S', 'H6W', 'I4N', 'I10N'], ['H4E', 'J12E', 'F9W', 'A8N', 'B4N'],
                 ['D3S', 'F7E', 'I1E', 'L7S', 'I10N']]

data_set_veteran = [['D4S', 'C7W', 'C14E', 'F8W', 'K1W', 'I6E', 'I7E', 'J14E'],
                    ['C2W', 'C7W', 'D11W', 'G6E', 'I1W', 'L2W', 'M8S', 'J14E'],
                    ['G3S', 'D5W', 'E11S', 'G11E', 'I7E', 'I11E', 'L4E', 'K12N'],
                    ['C3W', 'C11E', 'F2W', 'F11W', 'G10R', 'J1W', 'I8N', 'K14E']]

class ComputerService:
    def __init__(self, computer_board):
        self.__computer_board = computer_board

    @property
    def board(self):
        # Getter for the board
        return self.__computer_board

    def generate_planes(self):

        """
        This function generates planes for the computer
        :return:
        """

        data_set = []

        if self.__computer_board.difficulty == 0:
            data_set = data_set_easy[randint(0, 5)]
        elif self.__computer_board.difficulty == 1:
            data_set = data_set_normal[randint(0, 5)]
        elif self.__computer_board.difficulty == 2:
            data_set = data_set_hard[randint(0, 4)]
        elif self.__computer_board.difficulty == 3:
            data_set = data_set_veteran[randint(0, 3)]

        for item in data_set:
            x, y, orientation = 0, 0, 0
            items = list(item)
            if len(items) == 3:
                x, y, orientation = ord(items[0]) - 65, int(items[1]), items[2]
            elif len(items) == 4:
                x, y, orientation = ord(items[0]) - 65, int(items[1]) * 10 + int(items[2]), items[3]

            self.__computer_board.add_plane(x, y-1, orientation)

    def get_hit(self, x, y):
        """
        This function registers if a given input coordinates are crashes, hits or nothings and also marks the hit spot with X
        :param x:
        :param y:
        :return:
        """
        return self.__computer_board.get_hit(x, y)

    def move(self, x1, x2, y1, y2, cells, queue):
        """
        This function is the 'AI' of the computer, and it respects the difficulty of every game
        :param x1:
        :param x2:
        :param y1:
        :param y2:
        :param cells:
        :param queue:
        :return:
        """
        if self.__computer_board.difficulty == 0:
            return self.move_easy(x1, x2, y1 ,y2)
        if self.__computer_board.difficulty == 1:
            return self.move_medium(cells)
        if self.__computer_board.difficulty > 1:
            return self.move_hard(queue)


    def move_easy(self, x1, x2, y1, y2):
        """
        The most basic algorithm, it chooses random positions xd and hopes to hit a cabin
        :return: two integers (the coordinates)
        """
        # A cabin cannot be placed in such cell, because the plane would outrun the board. trivial_cells stores such cells.
        h = self.__computer_board.size
        trivial_cells = [(0, 0), (0, 1), (1, 0), (1, 1), (0, h-1), (0, h), (1, h-1), (1, h), (h-1, 0), (h-1, 1), (h, 0),
                         (h, 1), (h-1, h-1), (h-1, h), (h, h-1), (h, h)]

        x = randint(x2, x1)
        y = randint(y2, y1)
        while (self.__computer_board.data[x][y] == "X") or ((x, y) in trivial_cells):
            x = randint(0, h-1)
            y = randint(0, h-1)
        return x, y

    def move_medium(self, cells):
        if self.__computer_board.difficulty == 1:
            """
            If we hit a plane, we restrict our area of choice by a 5x5 square in order to find a cabin
            :return: two integers (the coordinates)
            """
            if len(cells) == 0:
                curr_x, curr_y = self.move_easy(self.__computer_board.size - 1, 0, self.__computer_board.size - 1, 0)
            else:
                x1 = max(0, cells[-1][0] - 2)
                y1 = max(0, cells[-1][1] - 2)
                x2 = min(self.__computer_board.size - 1, cells[-1][0] + 2)
                y2 = min(self.__computer_board.size - 1, cells[-1][1] + 2)
                curr_x, curr_y = self.move_easy(x1, x2, y1, y2)

            cells.clear()
            if self.__computer_board.data[curr_x][curr_y] == "A" or self.__computer_board.data[curr_x][curr_y] == "C":
                cells.append((curr_x, curr_y))

            return curr_x, curr_y

    def move_hard(self, queue):
        """
         For this hard difficulty, I was thinking of something like that: if we hit a plane, we check it's neighbours and
         this leads to a Lee's algorithm implementation(kinda AKA BFS).
         :return: two integers (the coordinates)
         """
        if len(queue) == 0:
            curr_x, curr_y = self.move_easy(self.__computer_board.size - 1, 0,  self.__computer_board.size - 1, 0)
            if self.__computer_board.data[curr_x][curr_y] == "A":
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if not (i == 0 and j == 0):
                            if curr_x + i < self.__computer_board.size and curr_y + j < self.__computer_board.size and \
                                    curr_x + i > 0 and curr_y + j > 0 and self.__computer_board.data[curr_x + i][curr_y + j] != "X":
                                queue.append((curr_x + i, curr_y + j))
        else:
            curr_x, curr_y = queue[0]
            queue.pop(0)
            if self.__computer_board.data[curr_x][curr_y] == "C":
                queue.clear()
            elif self.__computer_board.data[curr_x][curr_y] == "A":
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if not (i == 0 and j == 0):
                            if curr_x + i < self.__computer_board.size and curr_y + j < self.__computer_board.size and \
                                    curr_x + i > 0 and curr_y + j > 0 and self.__computer_board.data[curr_x + i][curr_y + j] != "X":
                                queue.append((curr_x + i, curr_y + j))

        return curr_x, curr_y