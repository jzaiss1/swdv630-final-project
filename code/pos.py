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

def processChoice(screens,choice,**kwargs):
  module = kwargs['me'].access
  screen = screens[module]

  if choice == 'in':
    # add a login prompt
    loadScreen(screens,module)
    return screen, module, kwargs

  if choice == 'open':
    print('Opening a ticket')
    # Call adding to an order function
    loadScreen(screens,module)
    kwargs['order'] = 'abc123'
    kwargs[kwargs['order']] = []
    return screen, module, kwargs

  if choice == 'add':
    id = int(input("Enter item id or 0 to exit "))
    while (id != 0):
      itemName, itemPrice = itemLookup(kwargs['db'],id)
      lineItem = LineItem(id,itemName,itemPrice,1)
      kwargs[kwargs['order']].append(lineItem)
      os.system('clear')
      printOrder(**kwargs)
      id = int(input("Enter item id or 0 to exit "))
    loadScreen(screens,module)
    return screen, module, kwargs

  if choice == 'fin':
    printOrder(**kwargs)
    return screen, module, kwargs
    
def printOrder(**kwargs):
  print("********************* Order {} *********************".format(kwargs['order']))
  print('{:>3} {:<40}  {}  {}'.format(' ID','Item','Qty','Price'))
  print("--------------------------------------------------------")
  total = 0
  for lineItem in kwargs[kwargs['order']]:
    total += lineItem.quantity * lineItem.price
    print('{:3} {:<40} {:3}  ${:5.2f}'.format(lineItem.id,lineItem.name,lineItem.quantity,lineItem.price))
  print("--------------------------------------------------------")
  print('Order {} Total {:>30} {:6.2f}'.format(kwargs['order'], '$', total))
  print("========================================================\n")

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

  kwargs = {'db' : itemsDB, 'me' : employees[0]}
  # System loads the main screen and waits for a valid response
  module = 'main'
  loadScreen(screens,module)
  choice = screens[module].getValidChoice()
  
  # Sample item lookup
  itemName, itemPrice = itemLookup(itemsDB,50)
  print(itemName, itemPrice)

  # Simulating a logon
  #me = employees[0]

  while choice != 'quit':
  # This needs to be moved to a function that processes responses  
    screen, module, kwargs = processChoice(screens,choice,**kwargs)
    choice = screen.getValidChoice()

main()