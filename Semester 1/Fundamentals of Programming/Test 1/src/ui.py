from functions import *
from datetime import datetime

def printMenu(startDate):
    print("Hello, user! Welcome to the code-runners game.")
    print(f"You have {returnCountTime(startDate)} seconds till the game ends so be fast with your predictions.")

def getRnsNCodes(option, randomNo):
    codes = getCodes(option, randomNo)
    runners = getRns(option, randomNo)

    print(f'Computer has reported {len(codes)} codes and {len(runners)} runners!')
    if len(codes) == 0 and len(runners) > 0:
        print(f'{runners} are runners')
    elif len(runners) == 0 and len(codes) > 0:
        print(f'{codes} are codes')

    else:
        print(f'{codes} are codes and {runners} are runners')

def main():
    randomNo = generateNumber()
    startDate = datetime.now().timestamp()

    while(True):
        if returnCountTime(startDate) < 0:
            print("Game lost! 60 seconds have been passed!")
            return

        printMenu(startDate)
        try:
            option = int(input(">>> Your guess is:"))
            if cheatCode(option) == True:
                print("Cheat code activated! The number is: " + str(randomNo))
            elif(checkExist(option, randomNo)) is False:
                print("Game over! No matching digits were found, the computer wins!")
                return
            if option == randomNo:
                print("Game over! Your guess was right so you win!")
                return
            if not cheatCode(option):
                getRnsNCodes(option, randomNo)
        except ValueError as ve:
            print(ve)
