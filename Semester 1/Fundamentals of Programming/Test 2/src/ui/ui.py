from random import randint

class UI:
    def __init__(self, taxi_service):
        self.__taxi_service = taxi_service

    def print_menu(self):
        print("Hello user, what can I do for you?")
        print("1. Add a ride")
        print("2. Simulate rides")
        print("3. Print Taxi States")
        print("4. Close the app")

    def add_ride(self):
        start_x = int(input("Please enter starting point x-axis: "))
        start_y = int(input("Please enter starting point y-axis: "))

        stop_x = int(input("Please enter ending point x-axis: "))
        stop_y = int(input("Please enter ending point y-axis: "))

        taxi = self.__taxi_service.add_ride(start_x, start_y, stop_x, stop_y)

        sorted_list = self.__taxi_service.get_sorted_list()
        for item in sorted_list:
            print(item)

    def generate_path(self):
        while True:
            start_x = randint(0, 100)
            start_y = randint(0, 100)
            stop_x = randint(0, 100)
            stop_y = randint(0, 100)

            if abs(start_x - stop_x) + abs(start_y - stop_y) > 9:
                return start_x, start_y, stop_x, stop_y

    def simulate_rides(self):

        number_of_rides = int(input("Please enter the number of simulated rides: "))

        while number_of_rides > 0:
            start_x, start_y, stop_x, stop_y = self.generate_path()
            taxi_id, initial_x, initial_y, initial_fare = self.__taxi_service.simulate_ride(start_x, start_y, stop_x, stop_y)

            sorted_list = self.__taxi_service.get_sorted_list()
            for item in sorted_list:
                print(item)

            self.__taxi_service.reset_taxi(taxi_id, initial_x, initial_y, initial_fare)

            number_of_rides -= 1


    def start(self):

        while True:
            self.print_menu()
            option = int(input(">>>"))

            if option == 4:
                return

            elif option == 2:
                self.simulate_rides()

            elif option == 1:
                self.add_ride()

            elif option == 3:
                sorted_list = self.__taxi_service.get_sorted_list()
                for item in sorted_list:
                    print(item)

            else:
                print("Wrong option!")
