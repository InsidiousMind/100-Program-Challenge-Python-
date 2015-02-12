import random

def pickRandom(range):
    randnum = random.randrange(range)
    return randnum
def flipManyCoins(numOfCoins):
    count = 0
    headCount = 0
    tailCount = 0
    while count < numOfCoins:
        if flipACoin() == "heads":
            headCount += 1
        else:
            tailCount += 1
        count += 1
    return 'You Had %d Tails and %d Heads!' % (tailCount, headCount)



def flipACoin():
    randNum = pickRandom(2)
    if randNum == 0:
       return "heads"
    else:
        return "tails"


def flipCoin(string):
    if string == "fifty":
        print(flipACoin())
    elif string == "chance":
        print("How many coins would you like to flip?")
        answer = input()
        try:
            print(flipManyCoins(int(answer)))
        except ValueError:
            print("please enter a number")
            flipCoin("chance")

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

def pickANum():
    print("Pick a number from 1-99")
    answer = input()
    try:
        if int(answer) > 99:
            print ("please pick a number from 1 to 99")
            pickANum()
        else:
            aRand = pickRandom(101)
            if int(answer) < aRand:
                print("Lower!")
                print("The Random Number Picked:",aRand)
            elif int(answer) > aRand:
                print("Higher!")
                print("The Number Picked:", aRand)
            else:
                print("Whoa! You got even!")
    except ValueError:
        print("please enter a NUMBER")
        pickANum()

def numPicked():
    firstRand = pickRandom(101)
    secRand = pickRandom(101)
    print("Your random number is:",firstRand)
    if firstRand < secRand:
        print("LOWER!")
        print("The Higher Number Picked:", secRand)
    else:
        print("HIGHER!")
        print("The Lower Number Picked:", secRand)

def isHigherLower():
    print("Do you want a number picked for you? (Y/n)")
    if input() == "Y":
        numPicked()
    else:
        pickANum()



promptUser()
