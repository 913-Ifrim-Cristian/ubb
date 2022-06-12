from src.domain.board import PlayerBoard, ComputerBoard
from src.services.computer import ComputerService
from src.services.player import PlayerService
from src.ui.ui import UI

difficulty_dict = {
    "easy": 0,
    "normal": 1,
    "hard": 2,
    "veteran": 3
}

difficulty = input("Please enter the difficulty of the game(easy/normal/hard/veteran): ")
difficulty = difficulty.lower()

if difficulty.strip() not in difficulty_dict:
    raise ValueError("Invalid difficulty")

player_board = PlayerBoard(difficulty_dict[difficulty])
computer_board = ComputerBoard(difficulty_dict[difficulty])

player = PlayerService(player_board)
computer = ComputerService(computer_board)

ui = UI(player, computer)
ui.start()

