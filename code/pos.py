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

# This function drives the PoS system by processing selections made from the various screens
# This is a console driven system but can be easily adapted to a UI by returning the same strings
# form onClick() or onPress() funtions in a UI
def processChoice(screens,**kwargs):
  print("\n\n")
  screen = screens[kwargs['me'].access]
  loggedIn = '*** {} logged in as {} ***\n'.format(kwargs['me'].id, kwargs['me'].access)
  checkoutOptions = ['cash','credit','debit']

  # Logging in functionality
  if kwargs['choice'] == 'in':
    print(loggedIn)
    kwargs['module'] = kwargs['me'].access
    loadScreen(screens, kwargs['module'])
    return screen, kwargs
  
  # Opening a new ticket functionality
  if kwargs['choice'] == 'open':
    print(loggedIn)
    kwargs['sale'] = Sale()
    print("********************* Sale {} **********************".format(kwargs['sale'].id))
    print('{:>3} {:<40}  {}  {}'.format(' ID','Item','Qty','Price'))
    print("--------------------------------------------------------\n")
    loadScreen(screens,kwargs['module'])
    return screen,kwargs

  # Adding items to an order functionality
  if kwargs['choice'] == 'add':
    os.system('clear')
    print('\n', loggedIn)
    print("********************* Sale {} **********************".format(kwargs['sale'].id))
    print('{:>3} {:<40}  {}  {}'.format(' ID','Item','Qty','Price'))
    print("--------------------------------------------------------\n")
    itemCount = kwargs['db'].query(Item).count()
    print('Item ids are 1 to {}'.format(itemCount))
    id = int(input("Enter item id or 0 to exit "))
    # Optimize the experiece to eliminate the need to use add from a menu to add a new item each time
    while (id != 0):
      print('\n\nItem ids are 1 to {}'.format(itemCount))
      itemName, itemPrice = itemLookup(kwargs['db'],id)
      lineItem = LineItem(id,itemName,itemPrice,1)
      kwargs['sale'].add(lineItem)
      os.system('clear')
      printOrder(**kwargs)
      id = int(input("Enter item id or 0 to exit "))
    printOrder(**kwargs)
    loadScreen(screens,kwargs['module'])
    return screen, kwargs

  # Removing an item functionality
  if kwargs['choice'] == 'rem':
    print(loggedIn)
    print("Last item added has been removed")
    iterator = kwargs['sale'].iterator()
    iterator.remove()
    printOrder(**kwargs)
    loadScreen(screens,kwargs['module'])
    return screen, kwargs

  # Completing the order functionality
  if kwargs['choice'] == 'fin':
    print(loggedIn)
    printOrder(**kwargs)
    # Change the module to checkout to add checkout options to the screen
    kwargs['module'] = 'checkout'
    loadScreen(screens,kwargs['module'])
    screen = screens[kwargs['module']]
    return screen,kwargs

  # Payment options functionality
  if kwargs['choice'] in checkoutOptions:
    print(loggedIn)
    print('checkout complete...\n')
    kwargs['module'] = kwargs['me'].access
    loadScreen(screens,kwargs['module'])
    return screen,kwargs

  # Logout functionality
  if kwargs['choice'] == 'out':
    print('{} logged out\n'.format(kwargs['me'].id))
    kwargs['module'] = 'main'
    loadScreen(screens,kwargs['module'])
    screen = screens[kwargs['module']]
    return screen,kwargs
    
def printOrder(**kwargs):
  print("\n")
  print("********************* Sale {} **********************".format(kwargs['sale'].id))
  print('{:>3} {:<40}  {}  {}'.format(' ID','Item','Qty','Price'))
  print("--------------------------------------------------------")
  total = 0
  
  iterator = kwargs['sale'].iterator()

  while iterator.has_next():
    item = iterator.next()
    total += item.quantity * item.price
    print('{:3} {:<40} {:3}  ${:5.2f}'.format(item.id,item.name,item.quantity,item.price))
  print("--------------------------------------------------------")
  print('Sale {} Total {:>30} {:7.2f}'.format(kwargs['sale'].id, '$', total))
  print("========================================================\n\n")

def bootstrap():
  # The system starts by loading items into an in memory database
  # First is the DB of items for sale
  itemsDB = loadItemsDB()

  # The system loads all employees into a list
  employees = loadEmployees()

  # The employees are used to create a list of login accounts
  # This is simulated, typically this would be in an identity management service

  # The system creates a dictionary of screens to display
  # This is console driven and would be adapted to do the same in a UI
  screens = loadScreens('data/screens.screen')

  return itemsDB, employees, screens

def main():
  
  itemsDB, employees, screens = bootstrap()
  
  # System loads the main screen and waits for a valid response
  loadScreen(screens,'main')
  choice = screens['main'].getValidChoice()

  kwargs = {'db' : itemsDB, 'me' : employees[0], 'module': '', 'choice' : choice}

  while kwargs['choice'] != 'quit':
    screen, kwargs = processChoice(screens,**kwargs)
    kwargs['choice'] = screen.getValidChoice()

main()