# Achi
Achi is an old strategy game first reported as being played in Ghana. Implement a console-based program that allows a human to play Achi against the computer. The game is played by two players using a 3x3 board. Each player has 4 pieces that they place on the board. The game is won by the player who first lines up 3 of their own pieces into a line, column, or diagonal. The game has two phases: placement and movement. The game rules are detailed as follows:
1. When the program is started, it displays an empty board **[0.5p]**
2. The **placement** phase of the game begins. The human(playing **X**) and computer(playing **O**) players take turns into placing their pieces on the board, in turn **[0.5p]**. Pieces can only be placed on an unoccupied square **[0.5p]**. The computer does not allow the player to win during placement **[1p]**.
3. If one of the players wins during placement, the game ends **[1p]**. Otherwise, it continues with the movement phase.
4. The **movement** phase of the game begins. The players take turns moving one of their own pieces into the unoccupied square. Pieces can be moved only to a square that is adjacent on a row, column, diagonally. The movement phase continues until one the players wins **[2p]**. The computer may move randomly. However, it must recognize and make an instant win move, if available **[1p]**.
5. User input is validated, and an error message is shown when trying to make an illegale move **[1p]**.
6. The game can be saved to a file at any time during play **[0.5p]**. When starting the program, you must choose between loading an existing game and starting a new one. Loading a game causes it to continue from where it was interrupted **[1p]**.

**Non-functional requirements:**

## Observations
- Make sure the program does not crash, regardless of user input.
- Implement a layered architecture solution.
- Provide specification and tests for the non-trivial, non-UI methods related to piece placement. Functionalities without specifications or tests are graded at 50% value.

Default **1p**.
