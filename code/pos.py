from employees import *
from screens import *
from itemsDB import *

# Use to simulate logging in
PASSWORD = 'pass'

def login(employees, id):
  return employee

def main():
  itemsDB = loadItemsDB()
  itemName, itemPrice = itemLookup(itemsDB,50)
  print(itemName, itemPrice)

  screens = loadScreens('data/screens.screen')
  employees = loadEmployees()
  me = employees[0]
  print(me.id, me.access)
  loadScreen(screens,'main')
  validChoice = screens['main'].getValidChoice()
  print("You chose: {}".format(validChoice))
  
  if validChoice == 'in':
    loadScreen(screens,me.access)

main()