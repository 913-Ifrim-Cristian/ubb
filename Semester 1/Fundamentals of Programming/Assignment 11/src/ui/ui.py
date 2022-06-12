class UI:
    def __init__(self, player, computer):
        self.__player = player
        self.__computer = computer

    def print_message(self):
        print("Hello, gamer! Welcome to Planes game. Based on your chosen difficulty, you need to place your planes.")
        print(f"You need to place {self.__player.board.number_of_planes} planes!\n")

    def request_planes(self):
        placed_planes = 0
        ok = 0
        while placed_planes < self.__player.board.number_of_planes:
            print(f"Placed planes: {placed_planes} / {self.__player.board.number_of_planes}.\n")

            coords = input("Please enter the coordinates of your cabin(e.g. A5, B7): ")
            orientation = input("Please enter the orientation of your cabin(e.g. N, S, E, W): ")

            coords = list(coords.strip().upper())
            x, y = 0, 0
            if len(coords) == 2:
                x, y = ord(coords[0]) - 65, int(coords[1])
            elif len(coords) == 3:
                x, y = ord(coords[0]) - 65, int(coords[1]) * 10 + int(coords[2])

            else:
                print("Wrong coordinates!")
                ok = 1

            if ok == 0:

                try:
                    self.__player.add_plane(x, y-1, orientation.strip().upper())
                    placed_planes += 1
                except Exception as e:
                    print(e)

            print("Player Board:")
            print(self.__player.board)
            ok = 0

    def request_hit(self):
        coords = input("Please enter the coordonates that you want to hit: ")
        coords = list(coords.strip().upper())
        print(coords)
        x, y = 0, 0
        if len(coords) == 2:
            x, y = ord(coords[0]) - 65, int(coords[1])
        elif len(coords) == 3:
            x, y = ord(coords[0]) - 65, int(coords[1]) * 10 + int(coords[2])
        else:
            raise ValueError("Wrong coordinates!")

        return self.__computer.get_hit(x, y)


    def start(self):
        self.print_message()
        print("Player Board:")
        print(self.__player.board)
        self.request_planes()

        print("The computer has placed his own planes! Let the game begin!")
        self.__computer.generate_planes()

        player_points = 0
        computer_points = 0

        cells = []
        queue = []

        while True:
            try:
                move = self.request_hit()
                if move == 1:
                    player_points += 1
                    print("You have crashed a plane!")
                elif move == 0:
                    print("You have hit the body of a plane!")
                else:
                    print("Nothing.")

                x, y = self.__computer.move(self.__computer.board.size-1, 0, self.__computer.board.size-1, 0, cells, queue)
                move = self.__player.get_hit(x, y)
                if move == 1:
                    computer_points += 1
                    print("Computer has crashed one of your planes!")
                elif move == 0:
                    print("Computer has hit one of your planes!")
                else:
                    print("Computer has hit nothing.")
            except Exception as e:
                print(e)

            print("Player Board:")
            print(self.__player.board)
            print("Computer Board:")
            print(self.__computer.board)

            if player_points == self.__player.board.number_of_planes:
                print("You won!")
                return
            if computer_points == self.__player.board.number_of_planes:
                print("You lost!")
                return
