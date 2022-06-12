# Solve the problem from the third set here

def solve():
    # Getting input data and creating a backup
    n = int(input("Enter the desired position of the sequence: "))
    N = n

    # Taking into account the case if user input is negative
    while n < 1:
        n = int(input("A sequence cannot have negative or null positions, please enter a positive number: "))

    # Printing the solution based on a specific algorithm
    """
    The alghoritm is: 
        if the number is lower than 4 that means is 1, 2 or 3 which is the start of the sequence
        else we check if the next number of the sequence is prime. If it is prime, we lower the remaining positions
        by one and do some checkings to see if we reached the wanted position. If the number is not prime, we create
        a list with its prime divisors and do the same checkings as above. When we reach the desired position we end
        the algorithm and print the solution
    """
    if n < 4:
        printSolution(n, n)
    else:
        N -= 3
        i = 4
        while (N > 0):
            if(checkPrime(i) == 0):
                dN = i
                while(dN > 1):
                    item = generateDiv(dN)
                    while(dN % item == 0):
                        dN //= item
                    if (N - item < 1):
                        printSolution(item, n)
                        N = 0
                        break
                    else:
                        N -= item
            else:
                if(N - 1 < 1):
                    printSolution(i, n)
                    N = 0
                else:
                    N -= 1
            i += 1


def printSolution(x, n):
    print("The element of the sequence with index " + str(n) + " is " + str(x) + ".")


def checkPrime(x):
    if x % 2 == 0 or x < 3:
        return x == 2
    d = 3
    while d * d <= x:
        if x % d == 0:
            return 0
        d += 2
    return 1

def generateDiv(x):
    d = 2
    while (x > 1):
        if x % d == 0:
            return d
        d += 1
    return 1


solve()
