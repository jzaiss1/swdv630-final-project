from employees import *
from screens import *

# Use to simulate logging in
PASSWORD = 'pass'

def main():
  screens = loadScreens('data/screens.screen')
  #me = Cashier('Elvis Presley')
  employees = loadEmployees()
  me = employees[0]
  print(me.id, me.access)
  loadScreen(screens,'main')
  validChoice = screens['main'].getValidChoice()
  print("You chose: {}".format(validChoice))
  
  if validChoice == 'in':
    loadScreen(screens,me.access)
  #printAllScreens(screens)
    # screen = Screen('PoS Main', 'data/main.screen')
    # screen.printScreen()
    # validChoice = screen.getValidChoice()
    # print("You chose: {}".format(validChoice))

main()