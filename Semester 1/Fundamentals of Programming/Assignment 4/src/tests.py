from functions import *

"""
General tests
"""
def test_createComplex():
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

def test_splitCommandArgs():
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

def test_parseComplex():
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

def test_getReal():
    """
    This function tests getReal function
    :return:
    """
    assert getReal(createComplex(5, 2)) == 5
    assert getReal(createComplex(8, 0)) == 8
    assert getReal(createComplex(100, -2)) == 100
    assert getReal([-20, 4]) == -20
    assert getReal([0, 0]) == 0

def test_getImg():
    """
    This function tests getImg function
    :return:
    """
    assert getImg(createComplex(5, 2)) == 2
    assert getImg(createComplex(8, 0)) == 0
    assert getImg(createComplex(100, -2)) == -2
    assert getImg([-20, 4]) == 4
    assert getImg([0, 0]) == 0

def test_getModulo():
    """
    This function tests if getModulo return correct values
    :return:
    """
    assert getModulo([2, 5]) == 29
    assert getModulo([-5, 0]) == 25
    assert getModulo([0, 25]) == 625
    assert getModulo(createComplex(10, -2)) == 104
    assert getModulo(createComplex(25, -5)) == 650

def test_setReal():
    """
    This function tests if setReal setter function works properly
    :return:
    """
    z = createComplex(5, 6)
    setReal(z, 20)
    assert getReal(z) == 20

    z = [-5, 60]
    setReal(z, -100)
    assert getReal(z) == -100

    z = [0, 20]
    setReal(z, 525)
    assert getReal(z) == 525

def test_setImg():
    """
    This function tests if setImg setter function works properly
    :return:
    """
    z = createComplex(5, 6)
    setImg(z, 20)
    assert getImg(z) == 20

    z = [-5, 60]
    setImg(z, -100)
    assert getImg(z) == -100

    z = [0, 20]
    setImg(z, 525)
    assert getImg(z) == 525

"""
Section A
"""

def test_addToList():
    """
    This function tests if addToList function works properly
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

def test_addCommand():
    """
    This function is a test function for addCommand
    :return:
    """
    l = [[], []]
    addCommand(l, "5+6i")
    assert l[1][-1] == [5, 6]

    addCommand(l, "               0                ")
    assert l[1][-1] == [0, 0]

    addCommand(l, "-              2i")
    assert l[1][-1] == [0, -2]

    addCommand(l, "-25 -         180i")
    assert l[1][-1] == [-25, -180]

def test_insertCommand():
    """
    This function tests if insertCommand does work properly
    :return:
    """
    l = [[], initList()]
    insertCommand(l, "5+3i at 4")
    assert l[1][4] == [5, 3]
    insertCommand(l, "6            at          2           ")
    assert l[1][2] == [6, 0]
    insertCommand(l, "-5i at 1")
    assert l[1][1] == [0, -5]
    insertCommand(l, "         90              +                  30i             at 8")
    assert l[1][8] == [90, 30]

"""
SECTION B
"""

def test_removeCommand():
    l = [[], initList()]
    item = l[1][4]
    length = len(l[1])
    removeCommand(l, "4")
    assert l[1][4] != item and len(l[1]) == length - 1

    item = l[1][2]
    length = len(l[1])
    removeCommand(l, "2")
    assert l[1][2] != item and len(l[1]) == length - 1

    item = l[1][5:8]
    length = len(l[1])
    removeCommand(l, "5 to 7")
    assert l[1][5:8] != item and len(l[1]) == length - 3

def test_replaceCommand():
    l = [[], [[5, 2], [6, 0], [5, 2], [5, 6]]]
    replaceCommand(l, "5+2i with -2")
    assert l[1][0] == [-2, 0] and l[1][2] == [-2, 0]
    l = [[], [[2, 0], [6, 5], [2, 4], [20, 0], [6, 5]]]
    replaceCommand(l, "2                       with          6+5i")
    assert l[1][0] == [6, 5]
    replaceCommand(l, "6       + 5i             with        90            -30i")
    assert l[1][0] == [90, -30] and l[1][4] == [90, -30]

"""
SECTION D
"""
def test_sumOfComplex():
    l = [[], [[5, 0], [6, 6], [3, 2], [1, 0], [5, 5], [9, 0], [6, 3], [7, 5]]]
    assert sumOfComplex(l, 3, 6) == [21, 8]
    assert sumOfComplex(l, 0, 4) == [20, 13]

    l = [[], [[7, 0]]]
    assert sumOfComplex(l, 0, 0) == [7, 0]
    l = [[], [[2, 3], [5, 4], [3, 2]]]
    assert sumOfComplex(l, 0, 2) == [10, 9]

def test_productOfComplex():
    l = [[], [[5, 0], [6, 6], [3, 2], [1, 0], [5, 5], [9, 0], [6, 3], [7, 5]]]
    assert productOfComplex(l, 3, 6) == [135, 405]
    assert productOfComplex(l, 0, 4) == [-600, 900]

    l = [[], [[7, 0]]]
    assert productOfComplex(l, 0, 0) == [7, 0]
    l = [[], [[2, 3], [5, 4], [3, 2]]]
    assert productOfComplex(l, 0, 2) == [-52, 65]
    l[1].append([0,0])
    assert productOfComplex(l, 0, 3) == [0, 0]

"""
SECTION E
"""
def test_filterByReal():
    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [5, 0]]]
    filterByReal(list)
    assert list[1] == [[6,0], [0,0], [5, 0]]

    list = [[], [[2, 4], [5, 0], [0, 5], [5, 5], [3, 4]]]
    filterByReal(list)
    assert list[1] == [[5, 0]]

    list = [[], [[2,4], [2, 5], [6, 6], [4, 1], [0, -2], [6, 0]]]
    filterByReal(list)
    assert list[1] == [[6, 0]]

def test_filterByModulo():
    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [5, 0]]]
    filterByModulo(list, "<", 5)
    assert list[1] == [[0, -1], [0, 0]]

    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [5, 0]]]
    filterByModulo(list, "<", 10)
    assert list[1] == [[6,0], [0, -1], [5, 5], [0, 0], [5, 0]]

    list = [[], [[2, 4], [5, 0], [0, 5], [5, 5], [3, 4]]]
    filterByModulo(list, "<", 7)
    assert list[1] == [[2, 4], [5, 0], [0, 5], [3, 4]]

    list = [[], [[2, 4], [4, 5], [6, 6], [4, 1], [0, -2], [6, 0]]]
    filterByModulo(list, "=", 6)
    assert list[1] == [[6, 0]]

    list = [[], [[0, 10], [6, 8], [0, -1], [10, 0], [0, 0], [5, 0]]]
    filterByModulo(list, "=", 10)
    assert list[1] == [[0, 10], [6, 8], [10, 0]]

    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [5, 0]]]
    filterByModulo(list, ">", 5)
    assert list[1] == [[5, 10], [6, 0], [5, 5]]

    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]]
    filterByModulo(list, ">", 10)
    assert list[1] == [[5, 10], [6, 9]]

    list = [[], [[9, 4], [5, 0], [0, 5], [5, 5], [3, 4]]]
    filterByModulo(list, ">", 7)
    assert list[1] == [[9,4], [5, 5]]



def test_filterCommand():

    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [5, 0]]]
    filterCommand(list, "real")
    assert list[1] == [[6, 0], [0, 0], [5, 0]]

    list = [[], [[2, 4], [5, 0], [0, 5], [5, 5], [3, 4]]]
    filterCommand(list, "real")
    assert list[1] == [[5, 0]]

    list = [[], [[2, 4], [2, 5], [6, 6], [4, 1], [0, -2], [6, 0]]]
    filterCommand(list, "real")
    assert list[1] == [[6, 0]]

    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [5, 0]]]
    filterCommand(list, "modulo < 5")
    assert list[1] == [[0, -1], [0, 0]]

    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [5, 0]]]
    filterCommand(list, "modulo < 10")
    assert list[1] == [[6, 0], [0, -1], [5, 5], [0, 0], [5, 0]]

    list = [[], [[2, 4], [5, 0], [0, 5], [5, 5], [3, 4]]]
    filterCommand(list, "modulo < 7")
    assert list[1] == [[2, 4], [5, 0], [0, 5], [3, 4]]

    list = [[], [[2, 4], [4, 5], [6, 6], [4, 1], [0, -2], [6, 0]]]
    filterCommand(list, "modulo = 6")
    assert list[1] == [[6, 0]]

    list = [[], [[0, 10], [6, 8], [0, -1], [10, 0], [0, 0], [5, 0]]]
    filterCommand(list, "modulo = 10")
    assert list[1] == [[0, 10], [6, 8], [10, 0]]

    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [5, 0]]]
    filterCommand(list, "modulo > 5")
    assert list[1] == [[5, 10], [6, 0], [5, 5]]

    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]]
    filterCommand(list, "modulo > 10")
    assert list[1] == [[5, 10], [6, 9]]

    list = [[], [[9, 4], [5, 0], [0, 5], [5, 5], [3, 4]]]
    filterCommand(list, "modulo > 7")
    assert list[1] == [[9, 4], [5, 5]]

"""
SECTION F
"""
def test_addToBackup():
    """
    This function is a test function for addToBackup. For a proper testing I will test by calling actual commands
    such that it assures that the function works properly
    :return:
    """
    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]]
    filterCommand(list, "modulo > 10")
    assert list[0] == [[[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]]

    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]]
    filterCommand(list, "real")
    assert list[0] == [[[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]]

    addCommand(list, "5+3i")
    assert getBackupList(list) == [[6,0], [0, 0]]

    removeCommand(list, "0")
    assert getBackupList(list) == [[6,0], [0, 0], [5, 3]]


def test_popFromBackup():
    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]]
    filterCommand(list, "modulo > 10")
    popFromBackup(list)
    assert list[0] == []

    list = [[], [[5, 2], [6, 4]]]
    addCommand(list, "5+3i")
    addCommand(list, "6")
    popFromBackup(list)
    assert list[0] == [[[5, 2], [6, 4]]]

    list = [[], [[5, 2], [6, 4], [6, 6]]]
    removeCommand(list, "0")
    addCommand(list, "6")
    popFromBackup(list)
    assert list[0] == [[[5, 2], [6, 4], [6, 6]]]



def test_getBackupList():
    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]]
    filterCommand(list, "real")
    assert getBackupList(list) == [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]

    addCommand(list, "5+3i")
    assert getBackupList(list) == [[6,0], [0, 0]]

    removeCommand(list, "0")
    assert getBackupList(list) == [[6,0], [0, 0], [5, 3]]

def test_undoCommand():
    list = [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]]
    filterCommand(list, "real")
    undoCommand(list, None)
    assert list == [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]]

    addCommand(list, "5  + 3i")
    removeCommand(list, "0")
    undoCommand(list, None)
    assert list[1] == [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9], [5, 3]]

    replaceCommand(list, "6 + 9i with 3+2i")
    undoCommand(list, "2")
    assert list == [[], [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]]