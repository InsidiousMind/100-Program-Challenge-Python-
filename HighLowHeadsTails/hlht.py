import random


def flipManyCoins(numOfCoins):
    count = 0
    while count < numOfCoins:
        flipCoin("fifty")
        count += 1
def flipCoin(string):
    if string == "fifty":
        randnum = random.randrange(1)
        if randnum == 0:
            print("heads!")
        elif randnum == 1:
            print("tails!")
    elif string == "chance":
        print("How many coins do you like to flip?")
        answer = input()
        flipManyCoins(int(answer))




def promptUser():
    print("Heads/Tails or Higher/Lower?")
    answer = input()
    print("Are You Playing for a 50/50 flip? (Y/n)")
    Yn = input()
    if Yn == "Y":
        flipCoin("fifty")
    elif Yn == "n":
        flipCoin("chance")

promptUser()



