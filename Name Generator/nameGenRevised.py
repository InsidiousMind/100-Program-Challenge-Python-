import random

def sample(items):
    # the first argument can be omitted as it defaults to 0
    randomIndex = random.randrange(len(items))
    return items[randomIndex]

def promptForGender():
    genderList = ["male", "female"]

    response = input("What Name Gender would you like? (m/f) (enter 'r' for random)")
    response = response.lower()

    # convert user input into some sort of normalized gender format
    # this could stay "m" and "f" instead
    if response == "m":
        return "male"
    elif response == "f":
        return "female"
    elif response == "r":
        return sample(genderList)
    else:
        print ("please enter 'M' ,'F', or 'R' to initiate the Random Name Generator")

def genName():
    boyNames = ["Jack", "Andrew", "Mike", "Terry", "Torvald", "Gatsby"]
    girlNames = ["Alice", "Hana", "Clare", "Janet", "Daisy"]

    gender = promptForGender()

    if gender == "male":
        return sample(boyNames)
    elif gender == "female":
        return sample(girlNames)

print ("Welcome to the Simple Random Name Generator by Liquid Think!")
print (genName())
