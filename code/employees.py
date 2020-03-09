# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Final Project

import random
import string
import csv

# This is our base employee class
class Employee():
  def __init__(self, name):
    self.id = self.generateId(name)
    self.name = name
    self.hired = ""
    self.terminated = ""
    self.ssn = ""
    self.active = True

  # Employee ids are generated with the first three characters of the name and a random three digits
  def generateId(self, name):
    id = name[0:3].lower() + '-' + ''.join(random.choice(string.digits) for i in range(3))
    return id

  def terminate(self):
    self.active = False
    self.terminated = "today"

  def changeStatus(self):
    self.active = False

  def getId(self):
    return self.id

# Each employee type has a distnc class
# This can allow for handling different levels of functionality in the system
class Cashier(Employee):
  def __init__(self, name):
    super().__init__(name)
    self.access = 'cashier'
    self.hourlyRate = 15.00
    self.schedule = []

  def addShift(self, date):
    pass

  def changeSupervisor(self, manager):
    pass

class Manager(Employee):
  def __init__(self, name):
    super().__init__(name)
    self.access = 'manager'
    self.salary = 10000

class Admin(Employee):
  def __init__(self, name):
    super().__init__(name)
    self.access = 'admin'
    self.hourlyRate = 15.00
    self.schedule = []

  def addShift(self, date):
    pass

  def changeSupervisor(self, manager):
    pass

class Stocker(Employee):
  def __init__(self, name):
    super().__init__(name)
    self.access = 'stocker'
    self.hourlyRate = 15.00
    self.schedule = []

  def addShift(self, date):
    pass

  def changeSupervisor(self, manager):
    pass

# An Account object is used for signing into the system and is created
# at the time an employee is created
class Account():
  def __init__(self,id):
    self.id = id
    self.password = 'pass'

  def updatePassword(self,old,new):
    if self.password == old:
      self.password = new
    else:
      print('invalid password try again')

  def login(self,password):
    if self.password == password:
      return True
    else:
      print('Wrong Password')
      return False

# This is our object factory that allows us to create each type of employee
def loadEmployees():
  employees = []
  employeeFile = open('data/employees', 'r')
  created = False
  reader = csv.reader(employeeFile)
  for row in reader:
    if row[0] == 'cashier':
      employee = Cashier(row[1])
      created = True
    if row[0] == 'manager':
      employee = Manager(row[1])
      created = True
    if row[0] == 'admin':
      employee = Admin(row[1])
      created = True
    if row[0] == 'stocker':
      employee = Stocker(row[1])
      created = True
    if created:
      employees.append(employee)
      created = False
    else:
      print("Need a class for {} employees".format(row[0]))

  return employees