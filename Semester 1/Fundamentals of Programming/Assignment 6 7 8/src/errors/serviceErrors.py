class ServiceError(Exception):
    def __init__(self, message = "Invalid data! Please be careful with input data"):
        self.__message = message
        super().__init__(self.__message)