# Solve the problem from the first set here
def solve():
    # Getting input data
    x = int(input("Enter a number: "))
    X = x
    x += 1

    # Searching for the closer prime that is greater than the number given
    while checkPrime(x) != 1:
        x += 1

    # Printing the result
    print("The first prime number greater than " + str(X) + " is " + str(x) + ".")


# Basic prime checking algorithm
def checkPrime(x):
    if x % 2 == 0 or x < 3:
        return x == 2
    d = 3
    while d * d <= x:
        if x % d == 0:
            return 0
        d += 2
    return 1


solve()
