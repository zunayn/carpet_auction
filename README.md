# Carpet Auctioning System in Python.
Leverages the concepts of OOP in Python language to create a carpet auctioning system.

## A BRIEF SUMMARY OF THE PROGRAM

### Classes used in the program and their brief desription: *(defined in data.py)*:   


1. Inventory: Contains all the carpets for auctioning. Also contains
information about bidders, admins. It defines CRUD methods to operate on them.

2. Bidders: Users who can place a bid on a carpet object, and win the carpet
if their bid is the highest. They have access to their bids i.e updating bids
and cancelling bids.

3. Admins: Users who have special privileges and can operate on the inventory i.e
add new carpets to the inventory.

4. Carpets: Contain data regarding them and their status in the auction i.e
no. of bids left, highest and last bidder, stock status etc.


### ***About the program***:

- The program works with the help of menus. Depending on what kind of user is
using the program, it will give different options accordingly.

- Only admins can add carpets to the inventory. This is a special privilege they
have.

- Bidders can place their bids on a carpet, and multiple bidders can bid on one
single carpet. The maximum no. of bids on a carpet can be 7. So, when 7 bids are
placed on a carpet, it goes to the highest bidder. A bidder can also cancel their
bids.

- The login and separation of users is not robust, and is just an emulation.

***NOTE: A default admin user instance with username="admin", and password="admin"
is created when the program starts.***


### ***How to Use***:

- The program starts with a clean state, so you wil have to add carpets to
the inventory manually, as well as create the bidders manually in the
lifetime of the program.

- This is achieved by logging into the Admin dashboard(kind of), and adding
the carpets to the inventory thereafter. Then, you have to create the Bidders
separately and then bid on the carpets from the Bidder Menu/dashboard.


***This is a project I made to measure my Object Oriented Design skills,
and programming skills in general. Do give feedback on what you think I can
improve, because surely, there is a lot.***
