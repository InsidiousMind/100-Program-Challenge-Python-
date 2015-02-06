#REQUIRES a Name Database. In this case, nameDB.csv :)
#REQUIRES pyhyphen
#To Install pyhyphen:
#first install "pip" the python package manager
#then "sudo pip install pyhyphen"
#and you are good to go
#Written in Python 3

import csv
import random
from hyphen import Hyphenator
from hyphen.dictools import *

#Split all the names in the list into syllables using pyhyphen
def syllabizeNames(nameList):
  tempList = []
  for lang in ['en_US']:
    if not is_installed(lang): install(lang)
  en_US = Hyphenator('en_US')
  for item in nameList:
    tempList.append(en_US.syllables(item))
  return tempList

#Parse the names from the csv file and put them into a list
def parseNames(nameFile):
  tempList = []
  csv_f = open(nameFile)
  try:
    reader = csv.reader(csv_f)
    for row in reader:
      tempList.append(row[0])
  finally:
    csv_f.close()
  return syllabizeNames(tempList)

#sample a random index from given list of items
def sample(items):
    randomIndex = random.randrange(len(items))
    return items[randomIndex]

#Choose an item and return it. If the method chances upon an empty item,
#It skips over it and continues
def chooseItem(list, place):
  #just a local variable
  thirdIndex = sample(list)
  try:
    if place == 1:
      return sample(list)[0]
    elif place == 3:
      while len(thirdIndex) != 3:
        thirdIndex = sample(list)
      return thirdIndex[2]
  except IndexError:
    print("Whoops! Looks like we came across an empty name object. :(")

#generate a name using "Choose Item". Try to concatenate them, if not,
#it will spit out null
def genName(list):
  firstPart = chooseItem(list, 1)
  secondPart = chooseItem(list, 3)
  try:
    return firstPart + secondPart
  except TypeError:
    print("null")

    #Prompt the user for input.
    #if they dont enter a number tell em'
def promptUser():
  numOfNames = input("How Many Names Would You Like to Generate?")
  count = 0
  try:
    numOfNames = int(numOfNames)
    while count < numOfNames:
      print(genName(names))
      count += 1
  except ValueError:
    print("Please Enter a Number")

#parse the names, syllabalizing them
names = parseNames('nameDB.csv')

#Viola!
print("Welcome to the Random Name Generator by Liquid Think!")
promptUser()
print("Here are Your Name(s)!:")





