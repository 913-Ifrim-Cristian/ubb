import random

"""
  Write non-UI functions below
"""

def createComplex(real = 0, img = 0): #tested
    """
    This function creates a complex number using a list
    :param real: the real part of the number
    :param img: the imaginary part of the number
    :return: a list representing the complex number
    """
    return [real, img]

def getReal(l): #tested
    """
    This function is used to get the real part of a number
    :param l: the representation of a complex number
    :return: the real part of the number
    """
    return l[0]

def getImg(l): #tested
    """
    This function is used to get the imaginary part of a number
    :param l: the representation of a complex number
    :return: the imaginary part of the number
    """
    return l[1]

def getModulo(z): #tested
    """
    This function returns the modulo of a complex number, but squared
    :param z:
    :return:
    """
    real, img = getReal(z), getImg(z)
    return real*real + img*img

def addToList(l, z): #tested
    """
    This function adds a complex number to the list
    :param l: the list in which the number will be added
    :param z: the complex number that will be added
    :return:
    """
    l.append(z)


def initList():
    """
    This function creates the initial list with the 10 complex numbers required
    :return: the list with all 10 complex numbers ready to use
    """
    l = []
    i = 0
    while(i < 10):
        real = int(random.random() * 1000)
        img = int(random.random() * 1000)
        addToList(l, createComplex(real, img))
        i += 1
    return l

def splitCommandArgs(userCommand): #tested
    """
    This function splits the command given by the user into command's name and it's parameters
    :param userCommand: the command given by the user
    :return:
    """
    userCommand = userCommand.lower()
    userCommand = userCommand.strip()

    commandTokens = userCommand.split(maxsplit = 1)
    commandName = commandTokens[0] if len(commandTokens) > 0 else None
    commandParams = commandTokens[1] if len(commandTokens) == 2 else None

    return commandName, commandParams

def parseComplex(params): #tested
    """
    This function parses a complex number given as a string and returns a list with the real part and the imaginary part of the number
    :param params:
    :return:
    """
    real, img = 0, 0
    found = 0
    params = params.replace(" ", "")
    params = params.replace("-", "+-")
    paramsTokens = params.split('+')
    for item in paramsTokens:
        if len(item) > 0 and item.find('i') == -1 and found == 0:
            real = int(item)
            found += 1
        elif item.find('i') != -1 and found < 2:
            found += 1
            img = int(item[:-1])
    return real, img

"""
Section A
"""

def addCommand(list, params): #tested
    """
    This function appends a complex number to the list
    :param list:
    :param params:
    :return:
    """
    try:
        real, imag = parseComplex(params)
        addToList(list, createComplex(real, imag))
    except:
        raise ValueError("Invalid parameters")

def insertCommand(list, params): #tested
    """
    This function adds a certain number at a given position
    :param list:
    :param params:
    :return:
    """
    params = params.replace(" ", "")
    paramsTokens = params.split("at")
    if len(paramsTokens) == 2:
        real, img = parseComplex(paramsTokens[0])
        pos = int(paramsTokens[1])
        if pos > len(list) or pos < 0:
            raise ValueError("Invalid position!")
        list.insert(pos, createComplex(real, img))
    else:
        raise ValueError("Invalid number of arguments!")

"""
Section B
"""

def removeCommand(list, params): #tested
    """
    This command removes a number at a given position, or a sequence of numbers from a start point to an end point
    :param list:
    :param params:
    :return:
    """
    params = params.strip()
    paramsTokens = params.split()

    if len(paramsTokens) == 1:
        pos = int(paramsTokens[0])
        if pos > len(list) or pos < 0:
            raise ValueError("Invalid position!")
        list.pop(pos)

    elif len(paramsTokens) == 3:
        start = int(paramsTokens[0])
        stop = int(paramsTokens[2])
        if paramsTokens[1] != "to":
            raise ValueError("Invalid parameters!")
        if start not in range(0, len(list)) or stop not in range(0, len(list)):
            raise ValueError("Invalid positions!")
        while stop >= start:
            list.pop(stop)
            stop -= 1
    else:
        raise ValueError("Invalid number of arguments!")

def replaceCommand(list, params): #tested
    """
    This function replaces all the occurences of a complex number with another complex number
    :param list:
    :param params:
    :return:
    """
    params = params.replace(" ", "")
    paramsTokens = params.split("with")

    if len(paramsTokens) == 2:
        real, img = parseComplex(paramsTokens[0])
        z1 = createComplex(real, img)
        real, img = parseComplex(paramsTokens[1])
        z2 = createComplex(real, img)
        found = 0
        for item in range(0, len(list)):
            if list[item] == z1:
                list[item] = z2
                found = 1
        if found == 0:
            raise ValueError("No occurences found")
    else:
        raise ValueError("Invalid number of arguments!")

#Test functions
def __createComplex():
    """
    Testing createComplex number!
    :return:
    """
    assert createComplex(5, 2)                  == [5, 2]
    assert createComplex(0, -5)                 == [0, -5]
    assert createComplex(-4, 200)               == [-4, 200]
    assert createComplex(-100, -120)            == [-100, -120]
    assert createComplex(60, 0)                 == [60, 0]
    assert createComplex(421, -123)             == [421, -123]

def __splitCommandArgs():
    """
    This function tests if splitCommandArgs return the correct values
    :return:
    """
    assert splitCommandArgs("exit") == ("exit", None)
    assert splitCommandArgs("EXit") == ("exit", None)
    assert splitCommandArgs("add 5+6i") == ("add", "5+6i")
    assert splitCommandArgs("ADd 0") == ("add", "0")
    assert splitCommandArgs("ADD -i") == ("add", "-i")
    assert splitCommandArgs("insert 6+3i at 6") == ("insert", "6+3i at 6")
    assert splitCommandArgs("InSErT -5i at 2") == ("insert", "-5i at 2")
    assert splitCommandArgs("remove 12") == ("remove", "12")
    assert splitCommandArgs("REMOvE 5 to 11") == ("remove", "5 to 11")
    assert splitCommandArgs("replace 5+2i with 0            ") == ("replace", "5+2i with 0")
    assert splitCommandArgs("replace -4i with 2+2i") == ("replace", "-4i with 2+2i")
    assert splitCommandArgs("list                 ") == ("list", None)
    assert splitCommandArgs("list REAl 2 to 10  ") == ("list", "real 2 to 10")
    assert splitCommandArgs("lisT           real 2 TO 10  ") == ("list", "real 2 to 10")
    assert splitCommandArgs("list                modulo < 10") == ("list", "modulo < 10")

def __parseComplex():
    """
    This function is a test function for parseComplex
    :return:
    """
    assert parseComplex("5+3i")                                 == (5, 3)
    assert parseComplex("5 + 3i")                               == (5, 3)
    assert parseComplex("      5                +          3i") == (5, 3)
    assert parseComplex("5           ")                         == (5, 0)
    assert parseComplex("-10i")                                 == (0, -10)
    assert parseComplex("-   60i")                              == (0, -60)
    assert parseComplex("           90      -      60 i")       == (90, -60)
    assert parseComplex("-30 + 90i    ")                        == (-30, 90)
    assert parseComplex("-30 + 90i - 60")                       == (-30, 90)
    assert parseComplex("-30 + 90i + 60i - 30")                 == (-30, 90)
    assert parseComplex("0")                                    == (0, 0)

def __getReal():
    """
    This function tests getReal function
    :return:
    """
    assert getReal(createComplex(5, 2)) == 5
    assert getReal(createComplex(8, 0)) == 8
    assert getReal(createComplex(100, -2)) == 100
    assert getReal([-20, 4]) == -20
    assert getReal([0, 0]) == 0

def __getImg():
    """
    This function tests getImg function
    :return:
    """
    assert getImg(createComplex(5, 2)) == 2
    assert getImg(createComplex(8, 0)) == 0
    assert getImg(createComplex(100, -2)) == -2
    assert getImg([-20, 4]) == 4
    assert getImg([0, 0]) == 0


def __addToList():
    """
    This function tests if addToList function works properly
    :param l:
    :return:
    """
    l = []
    addToList(l, [0, -2])
    assert l[-1] == [0, -2]

    addToList(l, [5, 0])
    assert l[-1] == [5, 0]

    addToList(l, [100, -25])
    assert l[-1] == [100, -25]

    addToList(l, createComplex(-5, 6))
    assert l[-1] == [-5, 6]

    addToList(l, createComplex(90, 2))
    assert l[-1] == [90, 2]

def __getModulo():
    """
    This function tests if getModulo return correct values
    :return:
    """
    assert getModulo([2, 5]) == 29
    assert getModulo([-5, 0]) == 25
    assert getModulo([0, 25]) == 625
    assert getModulo(createComplex(10, -2)) == 104
    assert getModulo(createComplex(25, -5)) == 650

def __insertCommand():
    l = initList()
    insertCommand(l, "5+3i at 4")
    assert l[4] == [5, 3]
    insertCommand(l, "6            at          2           ")
    assert l[2] == [6, 0]
    insertCommand(l, "-5i at 1")
    assert l[1] == [0, -5]
    insertCommand(l, "         90              +                  30i             at 8")
    assert l[8] == [90, 30]


def __removeCommand():
    l = initList()
    item = l[4]
    length = len(l)
    removeCommand(l, "4")
    assert l[4] != item and len(l) == length - 1

    item = l[2]
    length = len(l)
    removeCommand(l, "2")
    assert l[2] != item and len(l) == length - 1

    item = l[5:8]
    length = len(l)
    removeCommand(l, "5 to 7")
    assert l[5:8] != item and len(l) == length - 3


def __addCommand():
    l = []
    addCommand(l, "5+6i")
    assert l[-1] == [5, 6]

    addCommand(l, "               0                ")
    assert l[-1] == [0, 0]

    addCommand(l, "-              2i")
    assert l[-1] == [0, -2]

    addCommand(l, "-25 -         180i")
    assert l[-1] == [-25, -180]

def __replaceCommand():
    l = [[5, 2], [6, 0], [5, 2], [5, 6]]
    replaceCommand(l, "5+2i with -2")
    assert l[0] == [-2, 0] and l[2] == [-2, 0]
    l = [[2, 0], [6, 5], [2, 4], [20, 0], [6, 5]]
    replaceCommand(l, "2                       with          6+5i")
    assert l[0] == [6, 5]
    replaceCommand(l, "6       + 5i             with        90            -30i")
    assert l[0] == [90, -30] and l[4] == [90, -30]

"""
  Write the command-driven UI below
"""

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
        for item in list:
            printComplex(item)

    else:
        params = params.strip()
        paramsTokens = params.split()

        if len(paramsTokens) == 4:
            if paramsTokens[0] == "real":
                start, stop = int(paramsTokens[1]), int(paramsTokens[3])
                if start not in range(0, len(list)) or stop not in range(0, len(list)):
                    raise ValueError("Invalid positions!")
                found = 0
                for item in range(start, stop+1):
                    if getImg(list[item]) == 0:
                        printComplex(list[item])
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
                    for item in list:
                        if getModulo(item) < no*no:
                            printComplex(item)
                            found = 1
                elif rel == ">":
                    for item in list:
                        if getModulo(item) > no*no:
                            printComplex(item)
                            found = 1
                elif rel == "=":
                    for item in list:
                        if getModulo(item) == no*no:
                            printComplex(item)
                            found = 1

                if found == 0:
                    raise ValueError("There are no complex numbers respecting that property!")

            else:
                raise ValueError("Wrong parameters!")
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
    print(">>> exit: Exits the program.")
    print("------------------------------------------------------------")

def main():
    """
    The core of the program
    In this function we register the commands of the user and do most of the things
    :return:
    """
    # declaring and initialising the list of complex numbers
    l = initList()

    # Creating a dictionary to store every command name
    commandDictionary = {"add": addCommand,
                         "insert": insertCommand,
                         "remove": removeCommand,
                         "replace": replaceCommand,
                         "list": listCommand
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

def __runTests():
    """
    This function run all test functions
    :return:
    """
    __parseComplex()
    __createComplex()
    __splitCommandArgs()
    __getReal()
    __getImg()
    __addToList()
    __getModulo()
    __insertCommand()
    __removeCommand()
    __addCommand()
    __replaceCommand()
    print("All tests succesfully passed")

main()
#__runTests()
