
def testInput(temp, unit):
    isFloat = isinstance(float(temp), float)
    unit = unit.upper()
    if isFloat == False:
        print("please enter a number")
        promptUser()
    elif unit not in ["C", "F", "K"]:
        print("Please enter 'C' 'F' or 'K'!")
        promptUser()

def convTemp(temp, unit):
    #Test the Input for Correctness
    testInput(temp, unit)
    temp1 = float(temp)
    if unit == "C":
        print( "It's %.2f Fareignheight, and %.2f Kelvin!" % (C_F(temp1), C_K(temp1)))
    elif unit == "F":
        print("It's %.2f Celsius, and %.2f Kelvin!" % (F_C(temp1), F_K(temp1)))
    elif unit == "K":
        print( "It's %.2f Celsius, and %.2f Fareignheight!" % (K_C(temp1), F_K(temp1)))

def promptUser():
    print("What's the Temperature?")
    temp = input()
    print("What's the Unit? ((C)elsius,(K)elvin,(F)areignheight")
    unit = input()
    convTemp(temp, unit)

def C_K(a):
    return a + 273.15

def F_K(a):
    a = F_C(a)
    return C_F(a)

def C_F(a):
    return ((a*9)/5)+32


def F_C(a):
    return ((a - 32) * 5)/9

def K_C(a):
    return a - 273.15

def K_F(a):
    a = K_C(a)
    return C_F(a)

promptUser()

