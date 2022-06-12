class ServiceError(Exception):
    def __init__(self, message):
        super().__init__(message)

class BoardError(Exception):
    def __init__(self, message):
        super().__init__(message)

