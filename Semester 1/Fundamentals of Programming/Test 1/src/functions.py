from random import randint
from datetime import datetime

def toList(number):
    """
    Converts a number to a list
    :param number:
    :return:
    """
    lst = []
    while(number > 0):
        lst.append(number % 10)
        number //= 10
    return lst

def checkExist(option, randomNo):
    """
    This function checks if there are existing digits from the input option into the generated number
    :return:
    """
    lst = toList(randomNo)
    while(option > 0):
        c = option % 10
        if c in lst:
            return True
        option //= 10

    return False

def returnCountTime(startDate):
    """
    Counts the elapsed time
    :param startDate:
    :return:
    """
    finishDate = startDate + 60
    return int(finishDate - datetime.now().timestamp())



def cheatCode(option):
    """
    Check if is cheat code
    :param option:
    :return:
    """
    return option == 8086

def getCodes(option, randomNo):
    """
    This function returns the codes of a given option
    :param option:
    :param randomNo:
    :return:
    """
    rns = []
    listOption = toList(option)
    listRandom = toList(randomNo)
    for item in range(0, len(listRandom)):
        if listRandom[item] == listOption[item] and listRandom[item] not in rns:
            rns.append(listRandom[item])
    return rns

def getRns(option, randomNo):
    """
    Gets the runners
    :param option:
    :param randomNo:
    :return:
    """
    rns = []
    codes = getCodes(option, randomNo)
    listRandom = toList(randomNo)
    i = 0
    while(option > 0):
        c = option % 10
        if c not in rns or c not in codes:
            if c in listRandom and c != listRandom[i]:
                rns.append(c)
        i += 1
        option //= 10
    return rns


def generateNumber():
    """
    Generates a four digit number with distinct digits
    From a list with digits, if a digit is taken, we pop it out of the list
    :return:
    """
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    t = randint(1, len(l)-1)
    x1 = l[t]
    l.pop(t)

    t = randint(0, len(l)-1)
    x2 = l[t]
    l.pop(t)

    t = randint(0, len(l)-1)
    x3 = l[t]
    l.pop(t)

    t = randint(0, len(l)-1)
    x4 = l[t]
    l.pop(t)

    nr = x1*1000 + x2 * 100 + x3 * 10 + x4
    return nr