import random




def genName():

    boyNames = {0: "Jack",1: "Andrew", 2: "Mike",3: "Terry",4: "Torvald", 5: "Gatsby"}
    girlNames = {0: "Alice", 1: "Hana", 2: "Clare", 3: "Janet", 4: "Daisy"}
    genderList = {0: "M", 1: "F"}
    randGender = random.randrange(0, 2)
    randGirlName = random.randrange(0, len(girlNames))
    randBoyName = random.randrange(0, len(boyNames))

    askGender = raw_input("What Name Gender would you like? (m/f) (enter 'r' for random)")
    askGender = askGender.lower()

    if askGender != "m":
        if askGender != "r":
            if askGender !="f":
                print "please enter 'M' ,'F', or 'R' to initiate the Random Name Generator"
    if askGender == "r":
        if genderList[randGender] == "m":
            return boyNames[randBoyName]
        else:
            return girlNames[randGirlName]

    if askGender == "m":
        return boyNames[randBoyName]
    elif askGender == "f":
        return girlNames[randGirlName]



print "Welcome to the Simple Random Name Generator by Liquid Think!"
print genName()




