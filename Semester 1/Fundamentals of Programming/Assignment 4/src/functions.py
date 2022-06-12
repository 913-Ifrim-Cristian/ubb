"""
  Program functionalities module
"""
import random

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
        addToBackup(list)
        addToList(list[1], createComplex(real, imag))
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
        if pos > len(list[1]) or pos < 0:
            raise ValueError("Invalid position!")
        addToBackup(list)
        list[1].insert(pos, createComplex(real, img))
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
        if pos >= len(list[1]) or pos < 0:
            raise ValueError("Invalid position!")
        addToBackup(list)
        list[1].pop(pos)

    elif len(paramsTokens) == 3:
        start = int(paramsTokens[0])
        stop = int(paramsTokens[2])
        if paramsTokens[1] != "to":
            raise ValueError("Invalid parameters!")
        if start not in range(0, len(list[1])) or stop not in range(0, len(list[1])):
            raise ValueError("Invalid positions!")
        addToBackup(list)
        while stop >= start:
            list[1].pop(stop)
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
        addToBackup(list)
        for item in range(0, len(list[1])):
            if list[1][item] == z1:
                list[1][item] = z2
                found = 1
        if found == 0:
            popFromBackup(list)
            raise ValueError("No occurences found")
    else:
        raise ValueError("Invalid number of arguments!")

"""
SECTION D
"""
def setReal(z, value):
    """
    This function is a setter for the real part of a complex number
    :param z:
    :param value:
    :return:
    """
    z[0] = value

def setImg(z, value):
    """
    This function is a setter for the imaginary part of a complex number
    :param z:
    :param value:
    :return:
    """
    z[1] = value

def sumOfComplex(list, start, stop):
    """
    This function return the sum of complex numbers between two given positions
    :param list:
    :param start:
    :param stop:
    :return:
    """
    s = createComplex(0, 0)
    for item in range(start, stop+1):
        setReal(s, getReal(s) + getReal(list[1][item]))
        setImg(s, getImg(s) + getImg(list[1][item]))
    return s


def productOfComplex(list, start, stop):
    """
    This function returns the product of complex numbers between two given positions
    This respects the formula: (a+bi)*(c+di) = (ac - bd) + (ad+bc)i
    :param list:
    :param start:
    :param stop:
    :return:
    """
    p = createComplex(1, 0)
    for item in range(start, stop + 1):
        a, b = getReal(p), getImg(p)
        setReal(p, a * getReal(list[1][item]) - b*getImg(list[1][item]))
        setImg(p, a * getImg(list[1][item]) + b * getReal(list[1][item]))
    return p

"""
Section E
"""
def filterByReal(list):
    """
    This function filters the list and keeps only real numbers
    :param list:
    :return:
    """
    length, found = len(list[1]), 0
    for item in list[1]:
        if getImg(item) == 0:
            found = 1
            break
    if found == 0:
        raise ValueError("Couldn't filter the list as there are no real numbers!")
    addToBackup(list)
    for item in range(length-1, -1, -1):
        if getImg(list[1][item]) != 0:
            list[1].pop(item)

def filterByModulo(list, rel, no):
    """
    This function filters the list and keeps only the number that have their modulo respecting a given property
    :param list:
    :param rel:
    :param no:
    :return:
    """
    length, found = len(list[1]), 0
    if rel == "<":
        for item in list[1]:
            if getModulo(item) < no * no:
                found = 1
                break
        if found == 0:
            raise ValueError("Couldn't filter the list as there are no complex numbers with modulo < " + str(no) + "!")
        addToBackup(list)
        for item in range(length - 1, -1, -1):
            if getModulo(list[1][item]) >= no * no:
                list[1].pop(item)
    elif rel == ">":
        for item in list[1]:
            if getModulo(item) > no * no:
                found = 1
                break
        if found == 0:
            raise ValueError("Couldn't filter the list as there are no complex numbers with modulo > " + str(no) + "!")
        addToBackup(list)
        for item in range(length - 1, -1, -1):
            if getModulo(list[1][item]) <= no * no:
                list[1].pop(item)
    elif rel == "=":
        for item in list[1]:
            if getModulo(item) == no * no:
                found = 1
                break
        if found == 0:
            raise ValueError("Couldn't filter the list as there are no complex numbers with modulo = " + str(no) + "!")
        addToBackup(list)
        for item in range(length - 1, -1, -1):
            if getModulo(list[1][item]) != no * no:
                list[1].pop(item)


def filterCommand(list, params):
    """
    This functions filters the list and keeps only the elements that respects a given property
    :param list:
    :param params:
    :return:
    """
    params = params.strip()
    paramsTokens = params.split()

    if len(paramsTokens) == 1:
        if paramsTokens[0] != "real":
            raise ValueError("Invalid parameters!")
        filterByReal(list)
    elif len(paramsTokens) == 3:
        if paramsTokens[0] != "modulo":
            raise ValueError("Invalid parameters!")
        rel, no = paramsTokens[1], int(paramsTokens[2])
        if rel not in ["<", "=", ">"]:
            raise ValueError("Wrong parameters!")
        filterByModulo(list, rel, no)
    else:
        raise ValueError("Invalid number of arguments!")

"""
SECTION F
"""
def addToBackup(list):
    """
    This function adds into history the old state of the list that will change its state in the following short future
    :param list:
    :return:
    """
    oldList = list[1][:]
    list[0].append(oldList)
def popFromBackup(list):
    """
    This function removes the last backup saved on the history
    The history works as a stack, so, the last element will be removed
    :param list:
    :return:
    """
    list[0].pop()

def getBackupList(list):
    """
    A getter function for the top element of the History stack
    :param list:
    :return:
    """
    return list[0][-1]

def undoOperation(list):
    """
    The actual undo operation which modifies the actual list
    :param list:
    :return:
    """
    list[1] = getBackupList(list)[:]
    popFromBackup(list)

def undoCommand(list, params):
    """
    This function does the ability of the user to undo the last operations that have been done
    As there are only 5 functions that modifies the list: add, insert, remove, replace and filter, we need to implement
    the backup only on those
    :param list:
    :param params:
    :return:
    """
    if params == None:
        steps = 1
    else:
        try:
            steps = int(params.strip())
        except:
            raise ValueError("Invalid parameters!")

    if len(list[0]) < steps:
        raise ValueError("Cannot undo because there were not performed such many operations!")
    while steps > 0:
        undoOperation(list)
        steps -= 1

