import random


def flipManyCoins(numOfCoins):
    count = 0
    while count < numOfCoins:
       flipCoin(numOfCoins)
       count += 1 

def flipCoin(string):
    if string == "fifty":
        randnum = random.randrange(1)
        if randnum == 0:
            print("heads!")
        else:
            print("tails!")
    elif string == "chance":
        print("How many coins do you like to flip?")
        answer = input()
        isInt = isinstance(int(answer), int)
        if isInt == False:
            print("please enter a number")
            flipCoin()
        else:
            flipManyCoins(int(answer))



def promptUser():
    print("CoinFlip or Higher/Lower?(C/H)")
    answer = input()
    if answer == "C":
        isCoinFlip()
    elif answer == "H":
        isHigherLower()

def isCoinFlip(): 
    print("Are You Playing for a 50/50 flip? (Y/n)")
    Yn = input()
    if Yn == "Y":
        flipCoin("fifty")
    elif Yn == "n":
        flipCoin("chance")
def isHigherLower():
    print("The unfinished Higher/Lower Method!")
 

promptUser()
