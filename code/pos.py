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

def processChoice(screens,**kwargs):
  print("\n\n")
  screen = screens[kwargs['me'].access]
  loggedIn = '*** {} logged in as {} ***\n'.format(kwargs['me'].id, kwargs['me'].access)
  checkoutOptions = ['cash','credit','debit']

  if kwargs['choice'] == 'in':
    # add a login prompt
    print(loggedIn)
    kwargs['module'] = kwargs['me'].access
    loadScreen(screens, kwargs['module'])
    return screen, kwargs

  if kwargs['choice'] == 'open':
    print(loggedIn)
    kwargs['sale'] = Sale()
    print("********************* Sale {} **********************".format(kwargs['sale'].id))
    print('{:>3} {:<40}  {}  {}'.format(' ID','Item','Qty','Price'))
    print("--------------------------------------------------------\n")
    loadScreen(screens,kwargs['module'])
    
    return screen,kwargs

  if kwargs['choice'] == 'add':
    os.system('clear')
    print('\n', loggedIn)
    print("********************* Sale {} **********************".format(kwargs['sale'].id))
    print('{:>3} {:<40}  {}  {}'.format(' ID','Item','Qty','Price'))
    print("--------------------------------------------------------\n")
    itemCount = kwargs['db'].query(Item).count()
    print('Item ids are 1 to {}'.format(itemCount))
    id = int(input("Enter item id or 0 to exit "))
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

  if kwargs['choice'] == 'rem':
    print(loggedIn)
    print("Last item added has been removed")
    iterator = kwargs['sale'].iterator()
    iterator.remove()
    printOrder(**kwargs)
    loadScreen(screens,kwargs['module'])
    return screen, kwargs

  if kwargs['choice'] == 'fin':
    print(loggedIn)
    printOrder(**kwargs)
    kwargs['module'] = 'checkout'
    loadScreen(screens,kwargs['module'])
    screen = screens[kwargs['module']]
    return screen,kwargs

  if kwargs['choice'] in checkoutOptions:
    print(loggedIn)
    print('checkout complete...\n')
    kwargs['module'] = kwargs['me'].access
    loadScreen(screens,kwargs['module'])
    return screen,kwargs

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

  # The system creates a dictionary of sceens to display
  # This is console driven and would be adapted to do the same in a UI
  screens = loadScreens('data/screens.screen')

  return itemsDB, employees, screens

def main():
  
  itemsDB, employees, screens = bootstrap()
  
  # System loads the main screen and waits for a valid response
  loadScreen(screens,'main')
  choice = screens['main'].getValidChoice()

  # Simulating a logon
  #me = employees[0]

  kwargs = {'db' : itemsDB, 'me' : employees[0], 'module': '', 'choice' : choice}

  # Sample item lookup
  # itemName, itemPrice = itemLookup(itemsDB,50)
  # print(itemName, itemPrice)

  while kwargs['choice'] != 'quit':
  # This needs to be moved to a function that processes responses  
    screen, kwargs = processChoice(screens,**kwargs)
    kwargs['choice'] = screen.getValidChoice()

main()