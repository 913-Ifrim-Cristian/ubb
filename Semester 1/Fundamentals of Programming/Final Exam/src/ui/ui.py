from src.errors.errors import ServiceError

class UI:
    def __init__(self, player_service, computer_service):
        self.__player_service = player_service
        self.__computer_service = computer_service

    def request_player_placement(self):
        i = int(input("Please enter the X-Axis coordonate of the piece: "))
        j = int(input("Please enter the Y-Axis coordonate of the piece: "))

        self.__player_service.place(i, j)

    def request_player_move(self):
        i = int(input("Please enter the X-Axis coordonate of the piece: "))
        j = int(input("Please enter the Y-Axis coordonate of the piece: "))

        x = int(input("Please enter the new X-Axis coordonate of the piece: "))
        y = int(input("Please enter the new Y-Axis coordonate of the piece: "))

        self.__player_service.move(i, j, x, y)
    def start(self):
        #New game
        print("Welcome to the Achi game. This is the game board!")
        print(self.__player_service.board)
        print("You will start the placement phase.")
        while True:
            #placement phase
            while(self.__player_service.number_of_pieces() < 4):
                try:
                    self.request_player_placement()
                    if self.__player_service.check_win() is True:
                        print("Congratulations, you have won the game!")
                        return
                    self.__computer_service.placement()
                    if self.__computer_service.check_win() is True:
                        print("Embrace failure, you have lost!")
                        return

                    print(self.__player_service.board)

                except Exception as se:
                    print(se)
            #movement phase
            print("Movement phase!")
            try:
                self.request_player_move()
                if self.__player_service.check_win() is True:
                    print("Congratulations, you have won the game!")
                    return
                self.__computer_service.move()
                if self.__computer_service.check_win() is True:
                    print("Embrace failure, you have lost!")
                    return

                print(self.__player_service.board)
            except Exception as e:
                print(e)

    def continue_game(self):
        if (self.__player_service.number_of_pieces() < 4):
            print("Game continues on placement phase!")
            print(self.__player_service.board)
        print(self.__player_service.board)
        while (self.__player_service.number_of_pieces() < 4):
            try:
                self.request_player_placement()
                if self.__player_service.check_win() is True:
                    print("Congratulations, you have won the game!")
                    return
                self.__computer_service.placement()
                if self.__computer_service.check_win() is True:
                    print("Embrace failure, you have lost!")
                    return

                print(self.__player_service.board)

            except Exception as se:
                print(se)
        # movement phase
        if self.__player_service.check_win() is True:
            print("Congratulations, you have won the game!")
            return
        if self.__computer_service.check_win() is True:
            print("Embrace failure, you have lost!")
            return
        print("Movement phase!")
        try:
            self.request_player_move()
            if self.__player_service.check_win() is True:
                print("Congratulations, you have won the game!")
                return
            self.__computer_service.move()
            if self.__computer_service.check_win() is True:
                print("Embrace failure, you have lost!")
                return

            print(self.__player_service.board)
        except Exception as e:
            print(e)