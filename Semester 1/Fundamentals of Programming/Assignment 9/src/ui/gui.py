import tkinter as tk
import traceback
from tkinter import messagebox
from tkinter import *

from src.domain.book import Book
from src.domain.client import Client
from src.repository.repository import Repo
from src.services.clientService import ClientService
from src.services.bookService import BookService

MAIN_COLOR = "#6b0d0a"
BG_COLOR = "#2b2b2b"

def show_error(self, *args):
    err = traceback.format_exception(*args)
    messagebox.showerror('Exception',err)

tk.Tk.report_callback_exception = show_error

class GUI:

    def __init__(self, bookService, clientService, rentService, undoService):
        self.__window = tk.Tk()
        self.__window.geometry("800x600")
        self.__window.resizable(0,0)
        self.__window.title("Library")
        self.__bg = PhotoImage(file="ui/bg.png")

        """
        Button Design
        """
        self.__fontFamily = ("Times New Roman", 18, "bold")
        self.__btnPaddingX = 200
        self.__btnPaddingY = 5
        self.__btnRelief = RAISED
        self.__btnActiveBG = "#cc6600"
        self.__btnBG = "#ff9933"
        self.__btnBorder = 3

        self.setBG()
        self.createLabels()
        self.createButtons()

        """
        SERVICES INIT
        """
        self.__bookService = bookService
        self.__clientService = clientService
        self.__rentService = rentService
        self.__undoService = undoService

    def run(self):
        self.__window.mainloop()

    def createLabels(self):
        Label(self.__window, text="Library Application v0.1", bg = self.__btnBG).pack()
        Label(self.__window, text="There you can do the following:", bg = self.__btnBG).pack()
        Label(self.__window, text="").pack()

    def createButtons(self):
        Label(self.__window, text="").pack()
        Label(self.__window, text="").pack()
        manage = Button(self.__window, text="Manage clients and books", bd=self.__btnBorder,
                        padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                        font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                        command = lambda: self.manageWindow()).pack()
        Label(self.__window, text="").pack()
        Label(self.__window, text="").pack()
        rent = Button(self.__window, text="Rent or return a book", bd=self.__btnBorder,
                      padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                      font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                      command = lambda: self.rentWindow()).pack()
        Label(self.__window, text="").pack()
        Label(self.__window, text="").pack()
        search = Button(self.__window, text="Search clients or books", bd=self.__btnBorder,
                        padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                        font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                        command = lambda: self.searchWindow()).pack()
        Label(self.__window, text="").pack()
        Label(self.__window, text="").pack()
        stats = Button(self.__window, text="Statistics", bd=self.__btnBorder,
                       padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                       font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                       command = lambda: self.statsWindow()).pack()
        Label(self.__window, text="").pack()
        Label(self.__window, text="").pack()
        undo = Button(self.__window, text="Undo/Redo operations", bd=self.__btnBorder,
                      padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                      font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                      command = lambda: self.undoWindow()).pack()

    def setBG(self):
        bgLabel = Label(self.__window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    def manageWindow(self):
        window = Toplevel(self.__window)
        window.geometry("800x700")
        window.resizable(0,0)
        window.title("Manage clients and books")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="Book section: ", bg=self.__btnBG, font = self.__fontFamily).pack()
        Label(window, text="").pack()
        btnBookAdd = Button(window, text="Add a book", bd=self.__btnBorder,
                            padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                            font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                            command=lambda:self.bookAdd(window)).pack()
        Label(window, text="").pack()
        btnBookRemove = Button(window, text="Remove a book", bd=self.__btnBorder,
                               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                               font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                               command=lambda: self.bookRemove(window)).pack()
        Label(window, text="").pack()
        btnBookUpdate = Button(window, text="Update a book", bd=self.__btnBorder,
                               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                               font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                               command=lambda: self.bookUpdate(window)).pack()
        Label(window, text="").pack()
        btnListBooks = Button(window, text="List books", bd=self.__btnBorder,
                              padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                              font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                              command=lambda: self.listBooks(window)).pack()
        Label(window, text="").pack()
        Label(window, text="Client section: ", bg=self.__btnBG, font = self.__fontFamily).pack()
        Label(window, text="").pack()
        btnAddClient = Button(window, text="Add a client", bd=self.__btnBorder,
                              padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                              font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                              command = lambda: self.clientAdd(window)).pack()
        Label(window, text="").pack()
        btnClientRemove = Button(window, text="Remove a client", bd=self.__btnBorder,
                                 padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                                 font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                                 command=lambda: self.clientRemove(window)).pack()

        Label(window, text="").pack()

        btnClientUpdate = Button(window, text="Update a client", bd=self.__btnBorder,
                                 padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                                 font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                                 command=lambda: self.clientUpdate(window)).pack()
        Label(window, text="").pack()

        btnListClients = Button(window, text="List clients", bd=self.__btnBorder,
                                padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                                font = self.__fontFamily, bg=self.__btnBG, activebackground = self.__btnActiveBG,
                                command=lambda: self.listClients(window)).pack()

    def listBooks(self, main):
        window = Toplevel(self.__window)
        main.destroy()
        window.geometry("1140x420")
        window.resizable(1, 0)
        window.title("Books List")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        scroll = Scrollbar(window, orient='vertical')
        scroll.pack(side=RIGHT, fill=Y)

        mylist = Listbox(window, yscrollcommand=scroll.set, height=420, font = self.__fontFamily, bg=self.__btnBG)

        for item in self.__bookService():
            mylist.insert(END, str(self.__bookService[item]))

        mylist.pack(side=TOP, fill=BOTH)
        scroll.config(command=mylist.yview)



    def listClients(self, main):
        window = Toplevel(self.__window)
        main.destroy()
        window.geometry("820x420")
        window.resizable(1, 0)
        window.title("Clients List")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        scroll = Scrollbar(window, orient='vertical')
        scroll.pack(side=RIGHT, fill=Y)

        mylist = Listbox(window, yscrollcommand=scroll.set, height=420, font = self.__fontFamily, bg=self.__btnBG)

        for item in self.__clientService():
            mylist.insert(END, str(self.__clientService[item]))

        mylist.pack(side=TOP, fill=BOTH)
        scroll.config(command=mylist.yview)


    def bookUpdate(self, main):
        bookID = IntVar()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Update a book")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="Book ID:", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=0)

        e1 = Entry(window, textvariable=bookID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        e1.grid(row=0, column = 1)

        Button(window, text="Proceed", bd=self.__btnBorder,
               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command=lambda: self.commitBookUpdate(window, bookID)).grid(row=1)

    def clientUpdate(self, main):
        bookID = IntVar()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Update a client")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="Client ID:", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=0)

        e1 = Entry(window, textvariable=bookID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        e1.grid(row=0, column=1)

        Button(window, text="Proceed", bd=self.__btnBorder,
               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command=lambda: self.commitClientUpdate(window, bookID)).grid(row=1)

    def commitBookUpdate(self, main, bookID):

        id = bookID.get()

        bookAuthor = StringVar()
        bookTitle = StringVar()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Update a book")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="Author", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=0)

        e2 = Entry(window, textvariable=bookAuthor, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        Label(window, text="Title", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=1)

        e3 = Entry(window, textvariable=bookTitle, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        e2.grid(row=0, column=1)
        e3.grid(row=1, column=1)

        Button(window, text="Update Title", bd=self.__btnBorder,
               padx=self.__btnPaddingX-150, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command = lambda: self.bookTitleUpdate(window, id, bookTitle)).grid(row=2, column = 1)
        Button(window, text="Update Author", bd=self.__btnBorder,
               padx=self.__btnPaddingX-150, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command = lambda: self.bookAuthorUpdate(main, id, bookAuthor)).grid(row=2, column = 2)
        Button(window, text="Update Both", bd=self.__btnBorder,
               padx=self.__btnPaddingX-150, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command = lambda: self.bookBothUpdate(window, id, bookAuthor, bookTitle)).grid(row=2, column = 3)

    def commitClientUpdate(self, main, bookID):
        id = bookID.get()

        clientName = StringVar()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Update a client")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="Name", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=0)

        e2 = Entry(window, textvariable=clientName, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        e2.grid(row=0, column=1)

        Button(window, text="Update client", bd=self.__btnBorder,
               padx=self.__btnPaddingX - 150, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command=lambda: self.clientUpdateName(window, id, clientName)).grid(row=2, column=1)

    def clientUpdateName(self, main, id, clientName):

        name = clientName.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Update a client")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.__undoService.addCommandToStack("cUpdate", [id, self.__clientService[id].name, name])

        self.__clientService.updateClient(id, name)

        Label(window, text=f"Client with ID: {id} succesfully updated!", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).pack()

    def bookTitleUpdate(self, main, id, bookTitle):

        newTitle = bookTitle.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Update a book")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.__undoService.addCommandToStack("bUpdate", [1, id, self.__bookService[id].title, newTitle])
        self.__bookService.updateTitle(id, newTitle)

        Label(window, text=f"Book with ID: {id} succesfully updated!", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).pack()

    def bookAuthorUpdate(self, main, id, bookTitle):

        newTitle = bookTitle.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Update a book")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.__undoService.addCommandToStack("bUpdate", [2, id, self.__bookService[id].author, newTitle])
        self.__bookService.updateAuthor(id, newTitle)

        Label(window, text=f"Book with ID: {id} succesfully updated!", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).pack()

    def bookBothUpdate(self, main, id, bookAuthor, bookTitle):

        newTitle = bookTitle.get()
        newAuthor = bookAuthor.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Update a book")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.__undoService.addCommandToStack("bUpdate", [3, id, self.__bookService[id].title, newTitle,
                                                         self.__bookService[id].author, newAuthor])
        self.__bookService.updateBook(id, newTitle, newAuthor)

        Label(window, text=f"Book with ID: {id} succesfully updated!", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).pack()

    def bookAdd(self, main):
        bookID = IntVar()
        bookAuthor = StringVar()
        bookTitle = StringVar()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Add a book")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="ID:", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=0)

        e1 = Entry(window, textvariable=bookID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        Label(window, text="Author", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=1)

        e2 = Entry(window, textvariable=bookAuthor, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        Label(window, text="Title", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=2)

        e3 = Entry(window, textvariable=bookTitle, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)

        Button(window, text="Add Book", bd=self.__btnBorder,
               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command = lambda: self.bookAddToRepo(window, bookID, bookAuthor, bookTitle)).grid(row=3)

    def bookAddToRepo(self, main, bookID, bookAuthor, bookTitle):
        window = Toplevel(self.__window)
        main.destroy()
        window.title("Add a book")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        id = bookID.get()
        author = bookAuthor.get()
        title = bookTitle.get()

        self.__bookService.addBook(id, author, title)
        self.__undoService.addCommandToStack("bAdd", Book(id, author, title))

        Label(window, text=f"Book with ID: {id} added succesfully!", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).pack()


    def bookRemove(self, main):
        window = Toplevel(self.__window)
        window.resizable(0, 0)
        window.title("Remove a book")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        bookID = IntVar()

        Label(window, text="ID:", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=0)

        e1 = Entry(window, textvariable=bookID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        e1.grid(row=0, column=1)

        Button(window, text="Remove Book", bd=self.__btnBorder,
               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command = lambda: self.bookRemoveByID(window, bookID)).grid(row=1)

    def bookRemoveByID(self, main, bookID):

        id = bookID.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Remove a book")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        opList = self.__rentService.deleteRentalsByBook(id)
        opList.append(["bRemove", Book(id, self.__bookService[id].author, self.__bookService[id].title,
                                       self.__bookService[id].getAvailability(),
                                       self.__bookService[id].getRentNumber())])
        del self.__bookService[id]

        self.__undoService.addCommandToStack("cascade", opList)

        Label(window, text=f"Book with ID: {id} succesfully deleted!", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).pack()

    def clientAdd(self, main):
        clientID = IntVar()
        clientName = StringVar()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Add a client")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="ID:", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=0)

        e1 = Entry(window, textvariable=clientID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        Label(window, text="Name:", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=1)

        e2 = Entry(window, textvariable=clientName, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)


        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        Button(window, text="Add Client", bd=self.__btnBorder,
               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command = lambda: self.clientAddToRepo(window, clientID, clientName)).grid(row=2)

    def clientAddToRepo(self, main, clientID, clientName):
        window = Toplevel(self.__window)
        main.destroy()
        window.title("Add a book")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        id = clientID.get()
        name = clientName.get()

        self.__clientService.addClient(id, name)
        self.__undoService.addCommandToStack("cAdd", Client(id, name))

        Label(window, text=f"Client with ID: {id} added succesfully!", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).pack()

    def clientRemove(self, main):
        window = Toplevel(self.__window)
        window.resizable(0, 0)
        window.title("Remove a client")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        bookID = IntVar()

        Label(window, text="ID:", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=0)

        e1 = Entry(window, textvariable=bookID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        e1.grid(row=0, column=1)

        Button(window, text="Remove client", bd=self.__btnBorder,
               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command=lambda: self.clientRemoveByID(window, bookID)).grid(row=1)

    def clientRemoveByID(self, main, bookID):

        id = bookID.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Remove a client")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        opList = self.__rentService.deleteRentalsByBook(id)
        opList.append(["cRemove", Client(id, self.__clientService[id].name,
                                         self.__clientService[id].activeRental(),
                                         self.__clientService[id].getDaysRented())])
        del self.__clientService[id]

        self.__undoService.addCommandToStack("cascade", opList)

        Label(window, text=f"Client with ID: {id} succesfully deleted!", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).pack()

    def rentWindow(self):

        "Rent or return a book"
        window = Toplevel(self.__window)
        window.geometry("400x400")
        window.resizable(0, 0)
        window.title("Rent or return a book")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        btnBookRent = Button(window, text="Rent a book", bd=self.__btnBorder,
                             padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                             font=self.__fontFamily, bg=self.__btnBG, activebackground=self.__btnActiveBG,
                             command=lambda: self.rentBook(window)).pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        btnBookRemove = Button(window, text="Return a book", bd=self.__btnBorder,
                               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                               font=self.__fontFamily, bg=self.__btnBG, activebackground=self.__btnActiveBG,
                               command=lambda: self.unrentBook(window)).pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        btnListBooks = Button(window, text="List Rentals", bd=self.__btnBorder,
                              padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                              font=self.__fontFamily, bg=self.__btnBG, activebackground=self.__btnActiveBG,
                              command=lambda: self.listRentals(window)).pack()
        Label(window, text="").pack()
        Label(window, text="").pack()


    def listRentals(self, main):
        window = Toplevel(self.__window)
        main.destroy()
        window.geometry("1024x420")
        window.resizable(1, 0)
        window.title("Rentals List")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        scroll = Scrollbar(window, orient='vertical')
        scroll.pack(side=RIGHT, fill=Y)

        mylist = Listbox(window, yscrollcommand=scroll.set, height=420, font=self.__fontFamily, bg=self.__btnBG)

        for item in self.__rentService():
            mylist.insert(END, str(self.__rentService[item]))

        mylist.pack(side=TOP, fill=BOTH)
        scroll.config(command=mylist.yview)

    def rentBook(self, main):
        bookID = IntVar()
        clientID = IntVar()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Rent a book")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="Book ID:", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=0)

        e1 = Entry(window, textvariable=bookID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        Label(window, text="Client ID:", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=1)

        e2 = Entry(window, textvariable=clientID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        e1.grid(row=0, column = 1)
        e2.grid(row=1, column=1)

        Button(window, text="Rent", bd=self.__btnBorder,
               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command=lambda: self.commitBookRent(window, bookID, clientID)).grid(row=2)

    def unrentBook(self, main):
        bookID = IntVar()
        clientID = IntVar()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Return a book")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="Book ID:", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=0)

        e1 = Entry(window, textvariable=bookID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        Label(window, text="Client ID:", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).grid(row=1)

        e2 = Entry(window, textvariable=clientID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        Button(window, text="Return by client ID", bd=self.__btnBorder,
               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command=lambda: self.unrentCommand(window, "c", clientID.get())).grid(row=2, column = 0)
        Button(window, text="Return by book ID", bd=self.__btnBorder,
               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command=lambda: self.unrentCommand(window, "b", bookID.get())).grid(row=2, column = 1)

    def unrentCommand(self, main, option, id):

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Return a book")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)


        if option == "b":
            rental = self.__rentService.returnBook(id, 1)

            self.__undoService.addCommandToStack("unrent", rental)
            Label(window, text=f"Book from rental: {rental} returned succesfully!", bd=self.__btnBorder,
                  padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
                  font=self.__fontFamily, bg=self.__btnBG).grid(row=0)
        elif option == "c":
            rental = self.__rentService.returnBook(id, 2)

            self.__undoService.addCommandToStack("unrent", rental)
            Label(window, text=f"Book from rental: {rental} returned succesfully!", bd=self.__btnBorder,
                  padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
                  font=self.__fontFamily, bg=self.__btnBG).grid(row=0)


    def commitBookRent(self, main, bookID, clientID):

        bID = bookID.get()
        cID = clientID.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.resizable(0, 0)
        window.title("Rent a book")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.__rentService.addNewRental(cID, bID)
        self.__undoService.addCommandToStack("rent", [bID, cID])

        Label(window, text=f"Book with ID: {bID} has been succesfuly rented to client with ID: {cID}!", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).pack()



    def searchWindow(self):
        "Rent or return a book"
        window = Toplevel(self.__window)
        window.geometry("400x400")
        window.resizable(0, 0)
        window.title("Search clients or books")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        btnBookSearch = Button(window, text="Search books", bd=self.__btnBorder,
                               padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                               font=self.__fontFamily, bg=self.__btnBG, activebackground=self.__btnActiveBG,
                               command = lambda: self.bookSearch(window)).pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        btnClientSearch = Button(window, text="Search clients", bd=self.__btnBorder,
                                 padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                                 font=self.__fontFamily, bg=self.__btnBG, activebackground=self.__btnActiveBG,
                                 command = lambda: self.clientSearch(window)).pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()

    def statsWindow(self):
        window = Toplevel(self.__window)
        window.geometry("600x500")
        window.resizable(0, 0)
        window.title("Statistics")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        btnAuthor = Button(window, text="Most rented author", bd=self.__btnBorder,
                           padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                           font=self.__fontFamily, bg=self.__btnBG, activebackground=self.__btnActiveBG,
                           command = lambda: self.windowMostRentedAuthors(window)).pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        btnBooks = Button(window, text="Most rented books", bd=self.__btnBorder,
                          padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                          font=self.__fontFamily, bg=self.__btnBG, activebackground=self.__btnActiveBG,
                          command = lambda: self.windowMostRentedBooks(window)).pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        btnClients = Button(window, text="Most rented clients", bd=self.__btnBorder,
                            padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                            font=self.__fontFamily, bg=self.__btnBG, activebackground=self.__btnActiveBG,
                            command = lambda: self.windowMostActiveClient(window)).pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()

    def undoWindow(self):
        window = Toplevel(self.__window)
        window.geometry("400x400")
        window.resizable(0, 0)
        window.title("Undo/Redo")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        btnUndo = Button(window, text="Undo", bd=self.__btnBorder,
                         padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                         font=self.__fontFamily, bg=self.__btnBG, activebackground=self.__btnActiveBG,
                         command = lambda: self.undo(window)).pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        btnRedo = Button(window, text="Redo", bd=self.__btnBorder,
                         padx=self.__btnPaddingX, pady=self.__btnPaddingY, relief=self.__btnRelief,
                         font=self.__fontFamily, bg=self.__btnBG, activebackground=self.__btnActiveBG,
                         command = lambda: self.redo(window)).pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()
        Label(window, text="").pack()


    def undo(self, main):
        self.__undoService("undo")

        window = Toplevel(self.__window)
        main.destroy()

        Label(window, text="Undo operation has been done succesfuly!", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).pack()

    def redo(self, main):
        self.__undoService("redo")

        window = Toplevel(self.__window)
        main.destroy()

        Label(window, text="Redo operation has been done succesfuly!", bd=self.__btnBorder,
              padx=self.__btnPaddingX - 100, pady=self.__btnPaddingY, relief=self.__btnRelief,
              font=self.__fontFamily, bg=self.__btnBG).pack()


    def bookSearch(self, main):

        bookID = IntVar()
        bookAuthor = StringVar()
        bookTitle = StringVar()

        window = Toplevel(self.__window)
        main.destroy()
        window.geometry("800x600")
        window.resizable(0, 0)
        window.title("Most Rented Authors")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Button(window, text="Search book by ID", bd=self.__btnBorder,
               padx=self.__btnPaddingX-100, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command = lambda: self.bookSearchID(window, bookID)).grid(row=0)

        e1 = Entry(window, textvariable=bookID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        Button(window, text="Search book by Author", bd=self.__btnBorder,
               padx=self.__btnPaddingX-100, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command = lambda: self.bookSearchAuthor(window, bookAuthor)).grid(row=1)

        e2 = Entry(window, textvariable=bookAuthor, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        Button(window, text="Search book by Title", bd=self.__btnBorder,
               padx=self.__btnPaddingX-100, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command = lambda: self.bookSearchTitle(window, bookTitle)).grid(row=2)

        e3 = Entry(window, textvariable=bookTitle, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)


    def bookSearchID(self, main, bookID):
        id = bookID.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.title("Search book by ID")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text=str(self.__bookService[id]), bd=self.__btnBorder,
              padx=self.__btnPaddingX-150, pady=self.__btnPaddingY, relief=self.__btnRelief,
              bg=self.__btnBG).pack()
    def bookSearchAuthor(self, main, bookAuthor):
        id = bookAuthor.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.geometry("1140x420")
        window.resizable(1, 0)
        window.title("Search books by Author")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        scroll = Scrollbar(window, orient='vertical')
        scroll.pack(side=RIGHT, fill=Y)

        mylist = Listbox(window, yscrollcommand=scroll.set, height=420, font=self.__fontFamily, bg=self.__btnBG)

        l = self.__bookService.searchBookByAuthor(id)

        for item in l:
            mylist.insert(END, str(item))

        mylist.pack(side=TOP, fill=BOTH)
        scroll.config(command=mylist.yview)

    def bookSearchTitle(self, main, bookAuthor):
        id = bookAuthor.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.geometry("1140x420")
        window.resizable(1, 0)
        window.title("Search book by Title")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        scroll = Scrollbar(window, orient='vertical')
        scroll.pack(side=RIGHT, fill=Y)

        mylist = Listbox(window, yscrollcommand=scroll.set, height=420, font=self.__fontFamily, bg=self.__btnBG)

        l = self.__bookService.searchBookByTitle(id)

        for item in l:
            mylist.insert(END, str(item))

        mylist.pack(side=TOP, fill=BOTH)
        scroll.config(command=mylist.yview)

    def clientSearch(self, main):

        clientID = IntVar()
        clientName = StringVar()

        window = Toplevel(self.__window)
        main.destroy()
        window.geometry("800x600")
        window.resizable(0, 0)
        window.title("Search Client")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Button(window, text="Search client by ID", bd=self.__btnBorder,
               padx=self.__btnPaddingX-100, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command = lambda: self.clientSearchID(window, clientID)).grid(row=0)

        e1 = Entry(window, textvariable=clientID, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        Button(window, text="Search client by Name", bd=self.__btnBorder,
               padx=self.__btnPaddingX-100, pady=self.__btnPaddingY, relief=self.__btnRelief,
               font=self.__fontFamily, bg=self.__btnBG,
               command = lambda: self.clientSearchName(window, clientName)).grid(row=1)

        e3 = Entry(window, textvariable=clientName, bd=self.__btnBorder, relief=self.__btnRelief,
                   font=self.__fontFamily, bg=self.__btnBG)

        e1.grid(row=0, column=1)
        e3.grid(row=1, column=1)

    def clientSearchID(self, main, clientID):
        id = clientID.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.title("Search client by ID")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        Label(window, text=str(self.__clientService[id]), bd=self.__btnBorder,
              padx=self.__btnPaddingX-150, pady=self.__btnPaddingY, relief=self.__btnRelief,
              bg=self.__btnBG).pack()

    def clientSearchName(self, main, clientName):
        id = clientName.get()

        window = Toplevel(self.__window)
        main.destroy()
        window.geometry("820x420")
        window.resizable(1, 0)
        window.title("Search client by Name")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        scroll = Scrollbar(window, orient='vertical')
        scroll.pack(side=RIGHT, fill=Y)

        mylist = Listbox(window, yscrollcommand=scroll.set, height=420, font=self.__fontFamily, bg=self.__btnBG)

        l = self.__clientService.searchClientByName(id)

        for item in l:
            mylist.insert(END, str(item))

        mylist.pack(side=TOP, fill=BOTH)
        scroll.config(command=mylist.yview)

    def windowMostRentedAuthors(self, main):

        window = Toplevel(self.__window)
        window.geometry("600x420")
        window.resizable(0, 0)
        window.title("Most Rented Authors")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        scroll = Scrollbar(window, orient='vertical')
        scroll.pack(side=RIGHT, fill=Y)

        mylist = Listbox(window, yscrollcommand=scroll.set, height=420, font=self.__fontFamily, bg=self.__btnBG)

        l = self.__bookService.mostRentedAuthor()

        for item in l:
            mylist.insert(END, f"Author: {item[0]} was rented {item[1]} times.")

        mylist.pack(side=TOP, fill=BOTH)
        scroll.config(command=mylist.yview)

        main.destroy()

    def windowMostRentedBooks(self, main):
        window = Toplevel(self.__window)
        window.geometry("1140x420")
        window.resizable(1, 0)
        window.title("Most Rented Books")

        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        scroll = Scrollbar(window, orient='vertical')
        scroll.pack(side=RIGHT, fill=Y)

        mylist = Listbox(window, yscrollcommand=scroll.set, height=420, font=self.__fontFamily, bg=self.__btnBG)

        l = self.__bookService.mostRentedBooks()

        for item in l:
            mylist.insert(END, str(item))

        mylist.pack(side=TOP, fill=BOTH)
        scroll.config(command=mylist.yview)

        main.destroy()

    def windowMostActiveClient(self, main):
        window = Toplevel(self.__window)
        window.geometry("820x420")
        window.resizable(1, 0)
        window.title("Most Active Clients")
        bgLabel = Label(window, image=self.__bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        scroll = Scrollbar(window, orient='vertical')
        scroll.pack(side=RIGHT, fill=Y)

        mylist = Listbox(window, yscrollcommand=scroll.set, height=420, font=self.__fontFamily, bg=self.__btnBG)

        l = self.__clientService.mostActiveClients()

        for item in l:
            mylist.insert(END, str(item))

        mylist.pack(side=TOP, fill=BOTH)
        scroll.config(command=mylist.yview)

        main.destroy()

