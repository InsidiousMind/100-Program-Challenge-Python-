import random


def flipManyCoins(numOfCoins):
    for item in numOfCoins:


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



def promptUser():
    print("Are You Playing for a 50/50 flip? (Y/n)")
    Yn = input()
    if Yn == "Y":
        flipCoin("fifty")
    elif Yn == "n":
        flipCoin("chance")

promptUser()


