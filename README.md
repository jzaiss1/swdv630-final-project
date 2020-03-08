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

### Logging In

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

### Starting an order

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

### Adding items

Once a ticket is open then items are added to the order by selecting the `add` function.  The range of valid item id's are displayed and the cashier is prompted for the ide of an item.
```
 *** elv-411 logged in as cashier ***

********************* Sale VGK091 **********************
 ID Item                                      Qty  Price
--------------------------------------------------------

Item ids are 1 to 140
Enter item id or 0 to exit
```
After each item is added to the order the screen refreshes with the new order and a running total.
```
Item ids are 1 to 140

********************* Sale VGK091 **********************
 ID Item                                      Qty  Price
--------------------------------------------------------
  1 12oz Drinking Jar w Lid & Straw            1  $ 2.00
--------------------------------------------------------
Sale VGK091 Total                              $    2.00
========================================================

Enter item id or 0 to exit
```
When the order is complete entering `0` returns to the cashier functions screen and the sale can be updated completed or canceled
```
********************* Sale VGK091 **********************
 ID Item                                      Qty  Price
--------------------------------------------------------
  1 12oz Drinking Jar w Lid & Straw            1  $ 2.00
 10 1988 Topps Cardinals Team Set              1  $ 2.00
120 Glass Bottle                               1  $ 6.00
122 Glass Dairy Milk Jug                       1  $ 1.25
138 How to Train Your Dragon DVD               1  $ 3.00
--------------------------------------------------------
Sale VGK091 Total                              $   14.25
========================================================

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

### Removing items

Select `rem` to remove the last item from the order
```
*** elv-411 logged in as cashier ***

Last item added has been removed

********************* Sale VGK091 **********************
 ID Item                                      Qty  Price
--------------------------------------------------------
  1 12oz Drinking Jar w Lid & Straw            1  $ 2.00
 10 1988 Topps Cardinals Team Set              1  $ 2.00
120 Glass Bottle                               1  $ 6.00
122 Glass Dairy Milk Jug                       1  $ 1.25
--------------------------------------------------------
Sale VGK091 Total                              $   11.25
========================================================

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

### Completing the sale

To complete the order and checkout choose the `fin` option to bring up the checkout screen
```
*** elv-411 logged in as cashier ***

********************* Sale VGK091 **********************
 ID Item                                      Qty  Price
--------------------------------------------------------
  1 12oz Drinking Jar w Lid & Straw            1  $ 2.00
 10 1988 Topps Cardinals Team Set              1  $ 2.00
120 Glass Bottle                               1  $ 6.00
122 Glass Dairy Milk Jug                       1  $ 1.25
--------------------------------------------------------
Sale VGK091 Total                              $   11.25
========================================================

********** Checkout **********
credit  Pay with credit
debit   Pay with debit
cash    Pay with cash
cancel  Cancel entire order
******************************

Please enter your choice:
```
Select the payment option and the sale is closed and the cashier is returned to the order entry screen
```
*** elv-411 logged in as cashier ***

checkout complete...

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

### Logging out

By selecting the `out` option the cashier is logged out and the system is returned to the main screen
```
elv-411 logged out

********** Pos Main **********
in      Login to the System
pass    Change password
quit    Exit the system
******************************

Please enter your choice:
```