# Simple menu class to display functions available for various operations
import csv
import os

class Screen():
  def __init__(self, title, fileName):
    self.title = title
    self.dict = self.getSelections(fileName)

  # What screens do we need
    # Main
    # Cashier
    # PoS Admin
    # Sales Manager
    # Inventory

  # Screens are loaded from *.screen files

  def getSelections(self,fileName):
    screenFile = open(fileName, 'r')
    kwargs = {}
    reader = csv.reader(screenFile)
    for row in reader:
      kwargs[row[0]] = row[1]
    screenFile.close()
    return kwargs

  def printScreen(self):
    os.system('clear')
    print("********** {} **********".format(self.title))
    for k,v in self.dict.items():
      print("{:<8}{}".format(k,v))

  def getValidChoice(self):
    # Loop unti a valid choice is made
    while True:
      choice = input("Please enter your choice: ")
      # Return the choice in lower if found in the sequence
      # Returning lower makes for a better user experience and returns consistent data 
      if choice.lower() in self.dict.keys():
        return choice.lower()       
      print("'{}' is an invalid choice".format(choice))

def loadScreens(fileName):
  screens = {}
  screenFile = open(fileName, 'r')
  reader = csv.reader(screenFile)
  for row in reader:
    s = Screen(row[1],row[2])
    screens[row[0]] = s
  return screens

def printAllScreens(screens):
  for k,v in screens.items():
    print(k)
    v.printScreen()

def loadScreen(screens,access):
  screens[access].printScreen()
