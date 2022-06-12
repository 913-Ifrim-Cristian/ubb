# Solve the problem from the second set here
def solve():
    # Getting input data
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    # Creating the frequence list
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Decomposing number1 in order to verify the property using the frequence list
    decompose(n1, l)

    # Checking the property and giving the result
    if(checkProperty(n2, l) == 1):
        print(str(n1) + " and " + str(n2) + " have the property P!")
    else:
        print(str(n1) + " and " + str(n2) + " does not have the property P!")

def decompose(x: int, l):
    while x > 0:
        l[x % 10] = 1
        x //= 10


def checkProperty(x: int, l):
    while(x > 0):
        if(l[x % 10] == 0):
            return 0
        x //= 10
    return 1

solve()
