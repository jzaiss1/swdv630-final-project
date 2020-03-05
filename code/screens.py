# Simple menu class to display functions available for various operations
import csv

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
    print("****** {} ******".format(self.title))
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

def main():
    screen = Screen('PoS Main', 'data/main.screen')
    screen.printScreen()
    validChoice = screen.getValidChoice()
    print("You chose: {}".format(validChoice))
    
main()
