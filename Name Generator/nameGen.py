import random

boyNames = {
    0: "Jack",
    1: "Andrew",
    2: "Mike",
    3: "Terry",
    4: "Torvald",
    5: "Gatsby"
}
girlNames = {0: "Alice", 1: "Hana", 2: "Clare", 3: "Janet", 4: "Daisy"}


def genName():
    askLength = raw_input("How many names do you want back? (enter 'r' for random length)")
    askGender = raw_input("What Name Gender would you like? (M/F/U) (enter 'r' for random)")
    genderList = ["M", "F"]
   # askLength = askLength.upper()
   #askGender = askGender.upper()

    if (askLength == "r" and askGender == "r"):
        randGender = random.randrange(0, 2)
        randGurlName = random.randrange(0, 5)
        randBoyName = random.randrange(0, 6)

        if genderList[randGender] == "M":
            return boyNames[randBoyName]
        else:
            return girlNames[randGurlName]

    if askLength == "r" and askGender == "M":
        return boyNames[randBoyName]
    elif askLength == "r" and askGender == "F":
        return girlNames[randGurlName]


print ("welcome to the random name generator!")
print (genName())
