from src.ui.ui import UI
from src.ui.gui import GUI
from src.repository.repository import Repo, BookFileRepo, ClientFileRepo, RentalFileRepo, PickleRepo,\
    BookJSONRepo, ClientJSONRepo, RentalJSONRepo
from src.services.clientService import ClientService
from src.services.rentService import RentService
from src.services.bookService import BookService
from src.services.undoService import UndoRedo
from src.services.validators import *
from settings import Settings

appSettings = Settings()

bookRepo, clientRepo, rentalRepo, generate = 0, 0, 0, False

if appSettings.repo() == "inMemory":
    bookRepo = Repo()
    clientRepo = Repo()
    rentalRepo = Repo()
    generate = True

elif appSettings.repo() == "textFiles":
    bookRepo = BookFileRepo(appSettings.books())
    clientRepo = ClientFileRepo(appSettings.clients())
    rentalRepo = RentalFileRepo(appSettings.rentals())
    generate = False

elif appSettings.repo() == "binaryFiles":
    bookRepo = PickleRepo(appSettings.books())
    clientRepo = PickleRepo(appSettings.clients())
    rentalRepo = PickleRepo(appSettings.rentals())
    generate = False

elif appSettings.repo() == "jsonFiles":
    bookRepo = BookJSONRepo(appSettings.books())
    clientRepo = ClientJSONRepo(appSettings.clients())
    rentalRepo = RentalJSONRepo(appSettings.rentals())
    generate = False

bookValidator = BookValidator()
clientValidator = ClientValidator()

bookService = BookService(bookRepo, bookValidator, generate)
clientService = ClientService(clientRepo, clientValidator, generate)
rentService = RentService(rentalRepo, bookRepo, clientRepo, generate)
undoService = UndoRedo(bookService, clientService, rentService)



def saveFiles():
    bookRepo._saveFile()
    clientRepo._saveFile()
    rentalRepo._saveFile()


if appSettings.ui() == "console":
    ui = UI(bookService, clientService, rentService, undoService)
    ui.start()

elif appSettings.ui() == "GUI":
    gui = GUI(bookService, clientService, rentService, undoService)
    gui.run()

if appSettings.repo() in ["textFiles", "binaryFiles", "jsonFiles"]:
    saveFiles()