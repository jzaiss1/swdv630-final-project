# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Final Project

import random
import string
import csv

class Employee():
  def __init__(self, name):
    self.id = self.generateId(name)
    self.name = name
    self.hired = ""
    self.terminated = ""
    self.ssn = ""
    self.active = True

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

class Account():
  def __init__(self,id):
    self.id = id
    self.password = 'pass'

  def updatePassword(self,old,new):
    if self.password == old:
      self.password = new
    else:
      print('invalid password try again')

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
    if created:
      employees.append(employee)
      created = False
    else:
      print("Need a class for {} employees".format(row[0]))

  return employees