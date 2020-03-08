# Final Project

John Zaiss (GitHub id jzaiss1)

SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1

This the a repo for my final project

## Point of Sale System

This is a generic point of sale system design.  Ideally it this system can be easislly modified for various buisiness types by modifying the setup data.

### Elements that are required for this system include

* A minimum of 12 use cases - fully elaborated!
* A rough sketch of the UI of the system to give yourself some grounding .
* Architecture Diagram showing major systems.
* Class Diagram for major classes in your system - 12-15 classes.
* Create a sequence diagram for 1-3 objects that realize one of your use cases.
* Python application using the 6+ major classes demonstrating the core functionality - GUIs are NOT required.

## Functionality Demo

This is a walk through of the console screens simulating the login of a cashier and creating an order

### Bootstrap

The system is bootstrapped with the following command `python pos.py`. This initializes the main screen as seen below

```
Using SQLAlchemy version 1.3.13

********** Pos Main **********
in      Login to the System
pass    Change password
quit    Exit the system
******************************

Please enter your choice:
```
By selecting the `in` option we simulate a login of a cashier by statically assigning `employee[0]` as the logged in user.  Upon successful login the user is displayed a screen with functions based on their access.  See the screen below for a successful cashier logon.
```
*** elv-411 logged in as cashier ***

********** Order entry **********
open    Open a new sales ticket
add     Add an item to an order
rem     Remove an item from the order
rev     Review total order
fin     Complete an order
out     Log out of the system
*********************************

Please enter your choice:
```
By selecting `open` a new sales ticket is opened and the screen is updated to show the new empty sales order.
```
*** elv-411 logged in as cashier ***

********************* Sale VGK091 **********************
 ID Item                                      Qty  Price
--------------------------------------------------------

********** Order entry **********
open    Open a new sales ticket
add     Add an item to an order
rem     Remove an item from the order
rev     Review total order
fin     Complete an order
out     Log out of the system
*********************************

Please enter your choice:
```
Once a ticket is open then items are added to the order by selecting the `add` function.  The range of valid item id's are displayed and the cashier is prompted for the ide of an item.
```
 *** elv-411 logged in as cashier ***

********************* Sale VGK091 **********************
 ID Item                                      Qty  Price
--------------------------------------------------------

Item ids are 1 to 140
Enter item id or 0 to exit
```
