#
# Write the implementation for A2 in this file
#

#We will use the random module for generating the first 10 numbers
import random

# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities

"""
    This function is used to print a complex number in the a + bi form.
    There are cases when a complex number has special notations, e.g. -2i
    or 1 + i, a real number. These cases are treated in this function
"""
def printComplex(l):
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

def readComplex():
    """
    We need an this function to read a complex number
    We take the real part and the imaginary part and
    return the value from the createComplex function
    :return:
    """
    real = int(input("Real part: "))
    img = int(input("Imaginary part(Do not write i!!!): "))

    return createComplex(real, img)

def readList(l):
    """
    With this function we do the #1 task in the assignment.
    We will read a list of number and then we will add them to the list
    :param l: the list that will be completed with complex numbers
    :return:
    """
    while True:
        n = int(input("Enter the number of complex numbers you want to read(Enter 0 to stop reading!): "))
        if n == 0:
            return
        while(n > 0):
            z = readComplex()
            addToList(l, z)
            n -= 1


def printResult(l, start, stop, cnt):
    """
    This function is needed to print the solution of the given properties
    :param l: is the list of complex number in which we search for the property
    :param start: the start of the sequence
    :param stop: the end of the sequence
    :param cnt: this is the property given(in case of mine, 1 and 5)
    :return:
    """
    if cnt == 1:
        print("The longest sequence of complex numbers that have their real parts strictly increasing is: ")
    else:
        print("The longest sequence of real numbers is: ")
    for i in range(start, stop):
        printComplex(l[i])

def printList(l):
    """
    This function prints the list of complex numbers, needed in option #2.
    :param l: is the list that needs to be printed
    :return:
    """
    for item in l:
        printComplex(item)

def printMenu():
    """
    This function prints the menu after every command is given
    :return:
    """
    print("Hello, user! Please select one of the following commands:")
    print("--------------------------------------------------------")
    print("\t#1 Read a list of complex numbers.")
    print("\t#2 Display the entire list.")
    print("\t#3 Display the longest sequence that respects the property: ")
    print("\t\ta. Numbers have a strictly increasing real part.")
    print("\t\tb. The longest sequence of real numbers.")
    print("\t#4 Exit the application.")
    print("--------------------------------------------------------")

def main():
    """
    This is the main function, which is the core of the program
    There we register the commands that are given by the user and solve
    the required problems
    :return:
    """
    l = initList()
    while True:
        printMenu()
        cmd = input("Please enter the desired command: ")
        if cmd == "4":
            return
        elif cmd == "3":
            ecmd = input("Please enter the property wanted (a/b): ")
            if ecmd == "a":
                l, start, stop, cnt = propertyIncreasing(l)
                printResult(l, start, stop, cnt)
            elif ecmd == "b":
                l, start, stop, cnt = propertyRealNo(l)
                printResult(l, start, stop, cnt)
            else:
                print("Invalid input, please select a or b!")
        elif cmd == "2":
            printList(l)
        elif cmd == "1":
            readList(l)
        else:
            print("Invalid command!")

# print('Hello A2')

# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

def createComplex(real = 0, img = 0):
    """
    This function creates a complex number using a list
    :param real: the real part of the number
    :param img: the imaginary part of the number
    :return: a list representing the complex number
    """
    return [real, img]

def getReal(l):
    """
    This function is used to get the real part of a number
    :param l: the representation of a complex number
    :return: the real part of the number
    """
    return l[0]

def getImg(l):
    """
    This function is used to get the imaginary part of a number
    :param l: the representation of a complex number
    :return: the imaginary part of the number
    """
    return l[1]

def addToList(l, z):
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


def propertyIncreasing(l):
    """
    This function returns the longest sequence that respects the first property
    The property is: numbers that have their real part increasing
    :param l: the list of complex numbers
    :return: the list, the start position, the end position and the id of the property
    """
    length, start, stop = 1, 0, 0
    cnt, i = 1, 0
    item, listLen = 1, len(l)

    while item < listLen:
        if getReal(l[item]) > getReal(l[item - 1]):
            cnt += 1
            if cnt > length:
                length = cnt
                start = i
                stop = item + 1
        else:
            i = item
            cnt = 1
        item += 1

    return l, start, stop, 1

def propertyRealNo(l):
    """
    This function returns the longest sequence that respects the second property
    The property is: real numbers
    :param l: the list of complex numbers
    :return: the list, the start position, the end position and the id of the property
    """
    length, start, stop = 0, 0, 0
    cnt, i = 0, 0
    item, listLen = 1, len(l)

    if getImg(l[0]) == 0:
        cnt = 1
        length = 1
        stop = 1

    while item < listLen:
        if getImg(l[item]) == getImg(l[item - 1]) and getImg(l[item]) == 0:
            cnt += 1
            if cnt > length:
                length = cnt
                start = i
                stop = item + 1
        elif getImg(l[item]) == 0 and cnt == 0:
            cnt += 1
            i = item
            if cnt > length:
                length = cnt
                start = item
                stop = item + 1
        else:
            i = item
            cnt = 0
        item += 1

    return l, start, stop, 2

# print('Hello A2'!) -> prints aren't allowed here!
main()