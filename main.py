from data import Inventory, Admin
from helpers import get_user, get_carpet, add_carpet
from helpers import place_bid, cancel_bid, login


def main():
    inventory = Inventory()
    admin = Admin("admin", "admin", inventory) # Default admin.
    main_menu(inventory)


def main_menu(inventory):
    """
    Main menu for the auction program. User can choose roles, edit existing
    bidders, or quit.
    """
    while True:

        print()
        print("[A]dmin page.")
        print("[B]idder page.")
        print("[N]ew bidder.")
        print("[D]elete bidder.")
        print("[Q]uit.")

        choice = input(">> ").lower()

        if choice.startswith("a"):
            user = get_user(inventory)

            if isinstance(user, Admin):
                admin_menu(inventory, user)
            else:
                print("Not an admin!")

        elif choice.startswith("b"):
            bidder = get_user(inventory)
            bidder_menu(inventory, bidder)

        elif choice.startswith("n"):
            username, password = login()
            bidder = inventory.add_bidder(username, password)

            bidder_menu(inventory, bidder)

        elif choice.startswith("d"):
            bidder = get_user(inventory)
            inventory.delete_bidder(bidder)
            print("Bidder deleted!")

        elif choice.startswith("q"):
            break

        else:
            print("Invalid input!")

def admin_menu(inventory, user):
    """
    Menu for admins contained by the inventory. User get basic options,
    and special privilege to add new carpet instances to inventory.
    """
    print("\nADMIN MENU: ")

    while True:

        print()
        print("[C]arpets.")
        print("[B]idders.")
        print("[A]dd carpet.")
        print("[R]eturn.")

        choice = input(">> ").lower()

        if choice.startswith("c"):
            print("Carpets in Inventory: \n")

            for carpet in inventory.carpets:
                print(carpet)

        elif choice.startswith("b"):
            print("Bidders: \n")

            for bidder in inventory.bidders:
                print(bidder)

        elif choice.startswith("a"):
            add_carpet(user)
            print("Carpet added to inventory!")

        elif choice.startswith("r"):
            break

        else:
            print("Invalid input!")

def bidder_menu(inventory, bidder):
    """
    Menu for bidder instances. User can place a bid on carpets,
    view active/non-active bids, work with them, or return to main menu.
    """
    print("\nBIDDER MENU:")

    while True:

        print()
        print("[A]vailable carpets.")
        print("[B]ids.")
        print("[C]urrent bids.")
        print("[W]on bids.")
        print("[P]lace bid.")
        print("[R]eturn.")

        choice = input(">> ").lower()

        if choice.startswith("b"):
            print("Bid history: \n")

            for bid in bidder.bids:
                print(bid)

        elif choice.startswith("c"):
            print("Active bids: \n")

            for bid in bidder.active_bids:
                print(bid)

            bid_options(inventory, bidder)

        elif choice.startswith("w"):
            for carpet in inventory.carpets:
                carpet.sell()

            print("Bids won in auction: \n")

            for bid in bidder.won:
                print(bid)

        elif choice.startswith("a"):
            print("Carpets available for bidding: \n")

            for carpet in inventory.carpets:
                print(carpet)

        elif choice.startswith("p"):
            place_bid(inventory, bidder)

        elif choice.startswith("r"):
            break

        else:
            print("Invalid input! ")

def bid_options(inventory, bidder):
    """
    Menu for bidder to perform operations on a carpet instance.
    User can cancel bid, increase bid price, or return to main menu.
    """

    while True:

        print()
        print("[C]ancel bid.")
        print("[I]ncrease bid.")
        print("[R]eturn.")

        choice = input(">> ").lower()

        if choice.startswith("c"):
            cancel_bid(inventory, bidder)

        elif choice.startswith("i"):
            carpet = get_carpet(inventory)
            new_price = int(input("New price: $"))

            bidder.increase_bid(carpet, new_price)

        elif choice.startswith("r"):
            break

        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()
