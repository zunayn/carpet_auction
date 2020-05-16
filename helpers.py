from getpass import getpass


def get_carpet(inventory):
    """
    Get carpet instance from inventory by id, and return it.

    Infinitely prompt user for a carpet ID, until a valid ID is given.
    """
    while True:

        try:
            id = int(input("Carpet ID: "))
            carpet = inventory[id]

        except ValueError:
            print("Please enter a valid Carpet ID!")

        else:
            return carpet

def get_user(inventory):
    """
    Get user(admin/bidder) instance from inventory by username, and return it.

    Infinitely prompt user for a carpet ID, until a valid ID is given.
    """
    while True:

        try:
            username = login()[0]
            user = inventory[username]

        except (ValueError, IndexError):
            print("User not found. Please enter a valid username!")

        else:
            return user

def add_carpet(admin):
    """
    Make a carpet instance and add it to inventory.
    (Privilege of Admin instances only).
    """
    print()
    width = int(input("Width: "))
    height = int(input("Height: "))
    price = int(input("Price: $"))
    fabric = input("Fabric: ")

    admin.add_carpet(width, height, fabric, price)

def place_bid(inventory, bidder):
    """
    Get carpet instance from inventory, and place a bid on it.
    """
    carpet = get_carpet(inventory)
    amount = int(input("Amount: "))
    bidder.bid(carpet, amount)


def cancel_bid(inventory, bidder):
    """
    Get carpet instance from inventory, and cancel bid if bidder has
    an active bid on the instance.
    """
    carpet = get_carpet(inventory)
    bidder.cancel_bid(carpet)
    print("Bid canceled!")

def login():
    """
    Prompt user for username and password(hidden), and return tuple
    containing both.
    """
    print()
    username = input("Username: ")
    password = getpass("Password: ")

    return username, password
