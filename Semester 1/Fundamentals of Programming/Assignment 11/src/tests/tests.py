import unittest

from src.domain.board import PlayerBoard, ComputerBoard
from src.services.player import PlayerService
from src.services.computer import ComputerService
from src.errors.errors import BoardError, ServiceError

class TestService(unittest.TestCase):

    def setUp(self) -> None:
        self.__player_board = PlayerBoard(1)
        self.__computer_board = ComputerBoard(1)
        self.__computer = ComputerService(self.__computer_board)
        self.__player = PlayerService(self.__player_board)

    def tearDown(self) -> None:
        pass

    def test_add_plane(self):
        self.__computer_board.add_plane(1, 5, 'N')
        self.assertEqual(len(self.__computer_board.planes), 1)

        with self.assertRaises(BoardError):
            self.__player.add_plane(-1, 5, 'N')

        with self.assertRaises(ServiceError):
            self.__player.add_plane(1, 5, 'a')

        self.__player_board.add_plane(1, 5, 'N')
        self.assertEqual(len(self.__player_board.planes), 1)
        self.assertEqual(self.__player_board.data[1][5], 'C')

        with self.assertRaises(BoardError):
            self.__player.add_plane(1, 5, 'N')

        with self.assertRaises(BoardError):
            self.__player.add_plane(5, 5, 'S')

    def test_validate_positions(self):

        with self.assertRaises(BoardError):
            self.__player_board.validate_positions(-1, 2, 'N')

        with self.assertRaises(BoardError):
            self.__player_board.validate_positions(5, -1, 'E')

        with self.assertRaises(BoardError):
            self.__player_board.validate_positions(1, 1, 'E')

    def test_get_hit(self):
        self.__computer_board.add_plane(1, 5, 'N')
        self.assertEqual(len(self.__computer_board.planes), 1)

        self.assertEqual(self.__computer_board.get_hit(1, 5), 1)
        self.assertEqual(self.__computer_board.data[1][5], 'X')

        self.__computer_board.add_plane(5, 5, 'N')
        self.assertEqual(len(self.__computer_board.planes), 2)

        self.assertEqual(self.__computer_board.get_hit(6, 5), 0)

        self.assertEqual(self.__computer_board.get_hit(8, 8), -1)




