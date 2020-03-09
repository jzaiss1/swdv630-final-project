# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Final Project

# Simple menu class to display functions available for various operations
import csv
import os

class Screen():
  def __init__(self, title, fileName):
    self.title = title
    self.dict = self.getSelections(fileName)

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
    title = "********** {} **********".format(self.title)
    footer = ''
    for char in title:
      footer += '*'
    footer += '\n\n'
    print(title)
    for k,v in self.dict.items():
      print("{:<8}{}".format(k,v))
    print(footer)

  def getValidChoice(self):
    # Loop unti a valid choice is made
    while True:
      choice = input("Please enter your choice: ")
      # Return the choice in lower if found in the sequence
      # Returning lower makes for a better user experience and returns consistent data 
      if choice.lower() in self.dict.keys():
        return choice.lower()       
      print("'{}' is an invalid choice".format(choice))

# Screens are loaded and returned as a dictionary of modules
# The screens.screen file defines the screen files used for each module
# The file format is
  # column 0 = module name
  # column 1 = display name
  # column 2 = relative file path
def loadScreens(fileName):
  screens = {}
  screenFile = open(fileName, 'r')
  reader = csv.reader(screenFile)
  # Each row in the screen file represents a function that can be called
  for row in reader:
    s = Screen(row[1],row[2])
    screens[row[0]] = s
  return screens

# Used for debugging when creating new screen files
def printAllScreens(screens):
  for k,v in screens.items():
    print(k)
    v.printScreen()

# This method is called to print the active screen
def loadScreen(screens,module):
  screens[module].printScreen()
