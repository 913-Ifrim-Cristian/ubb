from src.domain.board import Board
from src.service.player import PlayerService
from src.service.computer import ComputerService
from src.validators.validator import Validator
from src.ui.ui import UI

filename = "game.txt"

board = Board(filename)
validator = Validator()
computer = ComputerService(board, validator)
player = PlayerService(board, validator)

ui = UI(player, computer)

option = int(input("1. New game\n2. Continue last game\nPlease select an option: "))

if option == 1:
    ui.start()
elif option == 2:
    board.load_data()
    player.load_data()
    computer.load_data()
    ui.continue_game()
else:
    raise ValueError("Incorrect input! Please re-run and select another option")



