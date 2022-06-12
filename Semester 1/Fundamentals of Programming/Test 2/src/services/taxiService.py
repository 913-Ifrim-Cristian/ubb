from random import randint
from src.domain.taxi import Taxi
from src.repository.repository import RepoError

class TaxiService:
    def __init__(self, repo, number_of_taxis):
        self.__repo = repo

        id = 0
        while number_of_taxis > 0:
            x = randint(0, 100)
            y = randint(0, 100)

            try:
                self.__repo.add(Taxi(id, x, y))
                id += 1
                number_of_taxis -= 1
            except RepoError:
                pass

    def get_closest_taxi(self, start_x, start_y):
        taxi_id = 0
        taxi_distance = abs(start_x - self.__repo[taxi_id].x) + abs(start_y - self.__repo[taxi_id].y)
        for item in self.__repo():
            if abs(start_x - self.__repo[item].x) + abs(start_y - self.__repo[item].y) < taxi_distance:
                taxi_distance = abs(start_x - self.__repo[item].x) + abs(start_y - self.__repo[item].y)
                taxi_id = item

        return taxi_id


    def add_ride(self, start_x, start_y, stop_x, stop_y):
        taxi = self.get_closest_taxi(start_x, start_y)

        self.__repo[taxi].x = stop_x
        self.__repo[taxi].y = stop_y
        self.__repo[taxi].fare += abs(start_x - stop_x) + abs(start_y - stop_y)

        return taxi

    def simulate_ride(self, start_x, start_y, stop_x, stop_y):
        taxi = self.get_closest_taxi(start_x, start_y)

        initial_x = self.__repo[taxi].x
        initial_y = self.__repo[taxi].y
        initial_fare = self.__repo[taxi].fare

        self.__repo[taxi].x = stop_x
        self.__repo[taxi].y = stop_y
        self.__repo[taxi].fare += abs(start_x - stop_x) + abs(start_y - stop_y)

        return self.__repo[taxi].ID, initial_x, initial_y, initial_fare

    def reset_taxi(self, taxi_id, initial_x, initial_y, initial_fare):
        self.__repo[taxi_id].x = initial_x
        self.__repo[taxi_id].y = initial_y
        self.__repo[taxi_id].fare = initial_fare



    def get_sorted_list(self):
        new_list  = list(self.__repo.getList())[:]
        new_list.sort(reverse = True)
        return new_list


