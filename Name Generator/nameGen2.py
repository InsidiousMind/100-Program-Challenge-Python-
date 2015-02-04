#REQUIRES a Name Database. In this case, nameDB.csv :)
import csv
import random
from hyphen import Hyphenator
from hyphen.dictools import *

def syllabizeNames(nameList):
  tempList = []
  for lang in ['en_US']:
    if not is_installed(lang): install(lang)
  en_US = Hyphenator('en_US')
  for item in nameList:
    tempList.append(en_US.syllables(item))
  return tempList

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

def sample(items):
    randomIndex = random.randrange(len(items))
    return items[randomIndex]


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
    print("Whoops! Looks like we came accross an empty name object. :(")

def genName(list):
  firstPart = chooseItem(list, 1)
  secondPart = chooseItem(list, 3)
  try:
    return firstPart + secondPart
  except TypeError:
    print("null")
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


print("Welcome to the Random Name Generator by Liquid Think!")
print("Heres Your Name!:")
promptUser()





