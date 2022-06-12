import unittest
from src.domain.board import Board
from src.service.player import PlayerService
from src.service.computer import ComputerService
from src.validators.validator import Validator
from src.errors.errors import ServiceError


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.__board = Board("test.txt")
        self.__validator = Validator()
        self.__computer = ComputerService(self.__board, self.__validator)
        self.__player = PlayerService(self.__board, self.__validator)

    def test_board_data_load(self):
        """
        These tests might run once because the file modifies at every call of move/place, so, a good set to test this is
        X, ,O,O,X,X,O,O,X, (paste this in test.txt) - player wins
        :return:
        """
        self.__board.load_data()
        self.__computer.load_data()
        self.__player.load_data()
        self.assertTrue(self.__player.check_win())

    def test_computer_win(self):
        """
         O,O,O, ,X,X,O,X,X, -computer wins
        :return:
        """
        self.__board.load_data()
        self.__computer.load_data()
        self.__player.load_data()

        self.assertTrue(self.__computer.check_win())
    def test_game(self):
        self.__board.place('X', 0, 0)
        x = self.__board.return_player_pieces()
        self.assertEqual(x, [(0, 0)])

        self.__board.place('O', 1, 0)
        x = self.__board.return_computer_pieces()
        self.assertEqual(x, [(1, 0)])

        with self.assertRaises(ServiceError):
            self.__player.place(0, 0)

        self.__board.move('X', 0, 0, 1, 2)
        x = self.__board.return_player_pieces()
        self.assertEqual(x, [(1, 2)])

        self.__player.place(0, 2)
        x = self.__board.return_player_pieces()
        self.assertEqual(x, [(0, 2), (1, 2)])

        self.assertTrue(self.__board.is_occupied(1, 2))
        self.assertFalse(self.__board.is_occupied(0, 0))

        self.__computer.placement()
        self.assertEqual(len(self.__board.return_computer_pieces()), 2)

        self.__computer.placement()
        self.assertEqual(len(self.__board.return_computer_pieces()), 3)



