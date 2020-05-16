# Carpet Auctioning System in Python.
Leverages the concepts of OOP in Python language to create a carpet auctioning system.

## A BRIEF SUMMARY OF THE PROGRAM

### This program works on following "pillars" *(defined in data.py)*:   


1. Inventory, which contains all the objects for auctioning, information
about bidders, admins, and defines methods to operate on them.

2. Bidders, who can place a bid on a carpet object, and win the bid
if theirs is the highest. They have access to their bids i.e updating them
and cancelling them.

3. Admins, who have special privileges and can operate on the inventory i.e
add new carpets to the inventory.

4. Carpets themselves, who contain data regarding them and their status
in the auction.

*The API is used in helpers.py to modularize the code in main.py.*


### ***main.py*** **(Usecase of the API/ Implementation of the program)**:


- Menus (Main menu, Admin Menu, Bidder Menu): Dashboards which provide the
 user accessibility on the things they can work on (explained above)

- Each menu contains a limited number of options for the user.

***NOTE: A default admin user instance with username="admin", and password="admin"
is created when the program starts.***


### ***How to Use***:

- The program starts with a clean state, so you wil have to add carpets to
the inventory manually, as well as create the bidders manually in the
lifetime of the program.

- This is achieved by logging into the Admin dashboard(kind of), and adding
the carpets to the inventory thereafter. Then, you have to create the Bidders
separately and then bid on the carpets from the Bidder Menu/dashboard.


***This is just a project I made to measure my OOP design skills, and programming
skills in general. Do give feedback on what you think I can improve, because
surely, there is a lot.***
