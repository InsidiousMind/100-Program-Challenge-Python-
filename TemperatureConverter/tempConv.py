
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
        print( "It's %d Fareignheight, and %d Kelvin!" % (C_F(temp1), C_K(temp1)))
    elif unit == "F":
        print("It's %d Celsius, and %d Kelvin!" % (F_C(temp1), F_K(temp1)))
    elif unit == "K":
        print( "It's %d Celsius, and %d Fareignheight!" % (K_C(temp1), F_K(temp1)))

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
    answer = 0
    answer = int(a)
    answer *= 9
    answer /= 5
    answer += 32
    return answer

def F_C(a):
    answer = int(a)
    answer -= 32
    answer *= 5
    answer /= 9
    return answer

def K_C(a):
    return a - 273.15

def K_F(a):
    a = K_C(a)
    return C_F(a)

promptUser()

