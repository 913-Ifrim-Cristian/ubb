from src.ui.ui import UI
from src.ui.gui import GUI
from src.repository.repository import Repo
from src.services.clientService import ClientService
from src.services.rentService import RentService
from src.services.bookService import BookService
from src.services.undoService import UndoRedo
from src.services.validators import *

bookRepo = Repo()
clientRepo = Repo()
rentalRepo = Repo()

bookValidator = BookValidator()
clientValidator = ClientValidator()

bookService = BookService(bookRepo, bookValidator, True)
clientService = ClientService(clientRepo, clientValidator, True)
rentService = RentService(rentalRepo, bookRepo, clientRepo, True)
undoService = UndoRedo(bookService, clientService, rentService)

option = int(input("How do you want to start the program?\n1. Console\n2. GUI\n>>>"))

if option == 1:
    ui = UI(bookService, clientService, rentService, undoService)
    ui.start()
else:
    gui = GUI(bookService, clientService, rentService, undoService)
    gui.run()