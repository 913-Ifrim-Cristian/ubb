"""
  User interface module
"""

from tests import *

def printComplex(l):
    """
        This function is used to print a complex number in the a + bi form.
        There are cases when a complex number has special notations, e.g. -2i
        or 1 + i, a real number. These cases are treated in this function
    """
    real = str(l[0])
    sign = "+"
    img = str(l[1]) + "i"
    if l[1] < 0:
        img = str(-l[1]) + "i"
        sign = "-"
    elif l[1] == 0:
        img = ""
        sign = ""
    elif l[1] == 1:
        img = "i"
    if l[0] == 0:
        if(l[1] == 0):
            print("0")
        else:
            real = ""
            print(sign + img)
    else:
        print(real + " " + sign + " " + img)

"""
Section C
"""

def listCommand(list, params):
    """
    This function is doing the section 5 command
    It lists the list if there are no parameters or different properties if 'modulo' or 'real' keyword is specified
    :param list:
    :param params:
    :return:
    """
    if params == None:
        for item in list[1]:
            printComplex(item)

    else:
        params = params.strip()
        paramsTokens = params.split()

        if len(paramsTokens) == 4:
            if paramsTokens[0] == "real":
                start, stop = int(paramsTokens[1]), int(paramsTokens[3])
                if start not in range(0, len(list[1])) or stop not in range(0, len(list[1])):
                    raise ValueError("Invalid positions!")
                found = 0
                for item in range(start, stop+1):
                    if getImg(list[1][item]) == 0:
                        printComplex(list[1][item])
                        found = 1

                if found == 0:
                    raise ValueError("There are no real numbers in the given interval!")

            else:
                raise ValueError("Wrong parameters!")
        elif len(paramsTokens) == 3:
            if paramsTokens[0] == "modulo":
                rel, no = paramsTokens[1], int(paramsTokens[2])
                if rel not in ["<", "=", ">"]:
                    raise ValueError("Wrong parameters!")
                found = 0
                if rel == "<":
                    for item in list[1]:
                        if getModulo(item) < no*no:
                            printComplex(item)
                            found = 1
                elif rel == ">":
                    for item in list[1]:
                        if getModulo(item) > no*no:
                            printComplex(item)
                            found = 1
                elif rel == "=":
                    for item in list[1]:
                        if getModulo(item) == no*no:
                            printComplex(item)
                            found = 1

                if found == 0:
                    raise ValueError("There are no complex numbers respecting that property!")

            else:
                raise ValueError("Wrong parameters!")
        else:
            raise ValueError("Invalid number of arguments!")

"""
SECTION D
"""
def sumCommand(list, params):
    """
    This function prints the sum of the number between two given positions
    :param list:
    :param params:
    :return:
    """
    if params == None:
        raise ValueError("Invalid parameters!")

    params = params.strip()
    paramsTokens = params.split()

    if len(paramsTokens) == 3:
        start = int(paramsTokens[0])
        stop = int(paramsTokens[2])
        if paramsTokens[1] != "to":
            raise ValueError("Invalid parameters!")
        if start not in range(0, len(list[1])) or stop not in range(0, len(list[1])):
            raise ValueError("Invalid positions!")

        printComplex(sumOfComplex(list, start, stop))
    else:
        raise ValueError("Invalid number of arguments!")

def productCommand(list, params):
    """
    This function prints the sum of the number between two given positions
    :param list:
    :param params:
    :return:
    """
    if params == None:
        raise ValueError("Invalid parameters!")

    params = params.strip()
    paramsTokens = params.split()

    if len(paramsTokens) == 3:
        start = int(paramsTokens[0])
        stop = int(paramsTokens[2])
        if paramsTokens[1] != "to":
            raise ValueError("Invalid parameters!")
        if start not in range(0, len(list[1])) or stop not in range(0, len(list[1])):
            raise ValueError("Invalid positions!")

        printComplex(productOfComplex(list, start, stop))
    else:
        raise ValueError("Invalid number of arguments!")

def printCommands():
    """
    This function prints the commands that the user can use
    :return:
    """
    print("Hello, user! There is a list of what commands should you use: ")
    print("------------------------------------------------------------")
    print(">>> add <number>: Appends a complex number to the list.")
    print(">>> insert <number> at <position>: Inserts a complex number at the given position(The index starts from 0!!!). ")
    print(">>> remove <position>: Removes the number found at the given position.")
    print(">>> remove <start> to <stop>: Removes the number found at the positions start, start + 1, ...., stop.")
    print(">>> replace <number> with <number>: Replaces all occurrences of the first number with the second one.")
    print(">>> list: Displays the entire list of complex numbers.")
    print(">>> list real <start> to <stop>: Displays the real numbers between position start and position stop.")
    print(">>> list modulo [< | = | >] <number>: Displays the complex numbers that have their modulo respecting the given relation.")
    print(">>> sum <start> to <stop>: Displays the sum of the complex numbers between start position and stop position.")
    print(">>> product <start> to <stop>: Displays the product of the complex numbers between start position and stop position.")
    print(">>> filter real: Filter the list in order to keep only real numbers.")
    print(">>> filter modulo [< | = | >] <number>: Filter the list in order to keep only numbers that have their modulo respecting the given relation.")
    print(">>> undo <number>: Undo the last perfomed operation if no number is given, or undo multiple operations if a number is given.")
    print(">>> exit: Exits the program.")
    print("------------------------------------------------------------")

def main():
    """
    The core of the program
    In this function we register the commands of the user and do most of the things
    :return:
    """
    # declaring and initialising the list of complex numbers
    l = [[], initList()]
    # Creating a dictionary to store every command name
    commandDictionary = {"add": addCommand,
                         "insert": insertCommand,
                         "remove": removeCommand,
                         "replace": replaceCommand,
                         "list": listCommand,
                         "sum": sumCommand,
                         "product": productCommand,
                         "filter": filterCommand,
                         "undo": undoCommand
                        }
    # Printing the commands
    printCommands()

    # Handling commands
    while True:
        # Getting users input
        userCommand = input("cmd>>>")
        # Parsing command into command name and the parameters
        commandName, commandParams = splitCommandArgs(userCommand)
        # Doing the actual commands
        if commandName == "exit":
            return
        if commandName not in commandDictionary:
            print("Invalid command! Please write a correct command!")
        else:
            try:
                commandDictionary[commandName](l, commandParams)
            except ValueError as ve:
                print(ve)

def runTests():
    """
    This function run all test functions
    :return:
    """
    test_parseComplex()
    test_createComplex()
    test_splitCommandArgs()
    test_getReal()
    test_getImg()
    test_addToList()
    test_getModulo()
    test_insertCommand()
    test_removeCommand()
    test_addCommand()
    test_replaceCommand()
    test_setReal()
    test_setImg()
    test_sumOfComplex()
    test_productOfComplex()
    test_filterByReal()
    test_filterByModulo()
    test_filterCommand()
    test_addToBackup()
    test_popFromBackup()
    test_undoCommand()
    test_getBackupList()
    print("All tests succesfully passed")

