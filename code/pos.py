# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Final Project

from employees import *
from screens import *
from itemsDB import *

# Use to simulate logging in
PASSWORD = 'pass'

def login(employees, id):
  return employee

def main():
  # The system starts by loading items into an in memory database
  # First is the DB of items for sale
  itemsDB = loadItemsDB()

  # The system loads all employees into a list
  employees = loadEmployees()

  # The employees are used to create a list of login accounts
  # This is simulated, typically this would be in an identity management service

  # The system creates a dictionary of sceens to display
  # This is console driven and would be adapted to do the same in a UI
  screens = loadScreens('data/screens.screen')

  # System loads the main screen and waits for a valid response
  loadScreen(screens,'main')
  validChoice = screens['main'].getValidChoice()

  # Sample item lookup
  itemName, itemPrice = itemLookup(itemsDB,50)
  print(itemName, itemPrice)

  # Simulating a logon
  me = employees[0]
  print(me.id, me.access)

  # This needs to be moved to a function that processes responses  
  if validChoice == 'in':
    loadScreen(screens,me.access)

main()