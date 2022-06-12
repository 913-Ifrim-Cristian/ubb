from src.errors.serviceErrors import ServiceError

class BookValidator():
    """
    This class validates a book if it has correct input data
    """
    def validateBook(self, book):
        errMsg = ""
        if book.ID < 0:
            errMsg += "Invalid ID\n"
        if book.title == "":
            errMsg += "Invalid title\n"
        if book.author == "":
            errMsg += "Invalid author"

        if len(errMsg) > 0:
            raise ServiceError(errMsg)

class ClientValidator(object):
    """
    This class validates a client if it has correct input data
    """
    def validateClient(self, client):
        errMsg = ""
        if client.ID < 0:
            errMsg += "Invalid ID\n"
        if client.name == "":
            errMsg += "Invalid name"

        if len(errMsg) > 0:
            raise ServiceError(errMsg)

