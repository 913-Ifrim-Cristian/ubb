class RepoError(Exception):

    def __init__(self, message = "Repository Error! Please be careful with input data."):
        self.__message = message
        super().__init__(self.__message)