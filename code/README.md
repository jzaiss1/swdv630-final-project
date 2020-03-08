# Codef for Final Project

John Zaiss (GitHub id jzaiss1)

SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1

This section of the project hosts the application files for the Point of Sale System

## pos.py

This is the main driver for the application. This is used to boostrap the PoS system and drive all functions.  When exiting this application the whole system shuts down.

## employees.py

This is the class module for handling employee objects.  The objects defined in the module are:

* Employee()
* Cashier(Employee)
* Manager(Employee)
* Stocker(Employee)
* Admin(Employee)
* Account()

The Account() class is used to simulated account logons in lieu of an identity management system

## itemsDB.py

This is the class module for handling stock items for sale and inventory items that can be used to create new stock items.  This class also contains objects for creating sales and purchases.

* Item(Base)
* OrderIterator
* Sale
* LineItem

## screens.py

This class module is used to drive the various screens displayed throughout the PoS system.  This class is designed for a console driven system but could be replaced by a UI driven system with minimal changes to the PoS application.  

* Screen()
