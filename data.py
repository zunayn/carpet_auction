class Inventory:
    """
    Container class for carpet instances, bidder instances, admin instances.

    Defines methods to operate on the above listed instances.
    """
    def __init__(self):
        self._carpets = set()
        self.bidders = set()
        self.admins = set()

    @property
    def carpets(self):
        """Return set of carpets in inventory available for bidding."""
        return set(carpet for carpet in self._carpets if carpet.in_stock)

    @property
    def carpet_ids(self):
        """Return set containg carpet IDs of all carpets in inventory."""
        return set(carpet.id for carpet in self._carpets)

    def __usernames(self, users):
        """
        Make and return set containing usernames of User instances in users.

        users: collection containing User instances.
        """
        return set(user.username for user in users)

    @property
    def bidder_usernames(self):
        """Return set containing bidder usernames in inventory."""
        return self.__usernames(users=self.bidders)

    @property
    def admin_usernames(self):
        """Return set containing admin usernames in inventory."""
        return self.__usernames(users=self.admins)


    def delete_bidder(self, bidder):
        """
        Remove 'bidder' from self.bidders list, and cancel it's all active bids.

        bidder: instance of Bidder class.
        """
        self.bidders.remove(bidder)
        bidder.cancel_all_bids()

    def add_bidder(self, username, password):
        """
        Create a new Bidder instance, add it to self.bidders list,
        and return instance.
        Raise ValueError if bidder with same username already exists.
        """
        if not username in self.bidder_usernames:

            bidder = Bidder(username, password)
            self.bidders.add(bidder)
            return bidder

        else:

            raise ValueError("Bidder already exists! ")

    def __get_carpet(self, id):
        """
        Search for a carpet instance by id and return it.
        Raise ValueError if not found.
        """
        for carpet in self.carpets:
            if carpet.id == id:
                return carpet

        raise ValueError("Carpet was not found.")


    def __get_user(self, users, username):
        """
        Search for user instance by username and return it.
        Raise ValueError is no instance is found.

        users: collection containing User instances.
        """
        for user in users:
            if user.username == username:
                return user

        raise ValueError("User was not found!")

    def __getitem__(self, ind):
        """
        Get item by 'ind', from inventory instance, and return it.

        If type(ind) == int, interpret as carpet id and look for carpets.
        If type(ind) == str, interpret as username and look for users
        (admins and bidders).

        Raise IndexError if index is not valid.
        """
        if isinstance(ind, int):
            item = self.__get_carpet(ind)

        elif isinstance(ind, str):

            try:
                item = self.__get_user(self.bidders, ind)
            except ValueError:
                item = self.__get_user(self.admins, ind)

        else:
            raise IndexError("Not a valid index. Enter a username or carpet ID")

        return item

    def __str__(self):
        for carpet in self.carpets:
            print("{}\n".format(carpet))


    def __len__(self):
        return len(self._carpets)

class Carpet:
    """
    Defines a Carpet within an auctioning system.

    Has a one-to-many relationship with bidder instances.
    Carpet can be bid upon max. 7 times, and has a unique ID.
    """
    bids_left = 7

    def __init__(self, id, width, height, fabric, base_price):

        # Display attributes.
        self.fabric = fabric
        self.width = width
        self.height = height

        self.base_price = base_price
        self.bidders = dict()
        self.id = id

    @property
    def last_bidder(self):
        """Return the last bidder of carpet."""
        if len(self.bidders) > 0:
            last = list(self.bidders.keys())[-1] # Works for versions >= 3.6.
            return last
        else:
            return -1

    @property
    def highest_bidder(self):
        """Return the highest bidder of carpet."""
        sorted_d = sorted(self.bidders.items(), key=lambda x: x[1])
        bidder = sorted_d[-1][0]
        return bidder

    @property
    def in_stock(self):
        """Check if carpet can be bid upon (is in stock)."""
        return self.bids_left > 0

    def sell(self):
        """
        Add/Give carpet instance to the highest bidder, if there are no bids
        left.
        """
        if not self.in_stock:
            self.highest_bidder.won.append(self)

    @property
    def price(self):
        """Return the current bid price for carpet."""
        if self.bidders:
            return self.bidders[self.highest_bidder] # Return highest bid.
        else:
            return self.base_price


    def add_bidder(self, bidder, amount):
        """
        Add bidder instance to self.bidders dictionary mapping from the
        instance to the bid amount.
        Raise ValueError if 'bidder' is already the last bidder of carpet.
        """

        if self.last_bidder is not bidder:
            self.bids_left -= 1
            self.bidders[bidder] = amount

        else:
            raise ValueError("Bidder cannot be same as last bidder.")


    def __str__(self):
        details = "{} {}x{}".format(self.fabric, self.width, self.height)

        return "{} ID: {}, Highest Bid: ${}, In Stock: {}".format(
                                        details, self.id,
                                        self.price, self.in_stock)

    def __repr__(self):
        return "ID: {}, In Stock: {}".format(self.id, self.in_stock)


class User:
    """
    Defines a User having username and password.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return self.username


class Admin(User):
    """
    Defines an Admin which is-a User but has special privileges
    for the inventory.
    """
    def __init__(self, username, password, inventory):
        super().__init__(username, password)
        self.inventory = inventory

        self.inventory.admins.add(self) # Add admin to inventory.

    def add_carpet(self, width, height, fabric, price):
        """
        Make a carpet instance with a unique id, add it to self.inventory,
        and return it.
        """
        id = len(self.inventory.carpet_ids) + 1
        carpet = Carpet(id, width, height, fabric, price)
        self.inventory._carpets.add(carpet)

        return carpet

    def  __repr__(self):
        return "Admin: " + super().__repr__()



class Bidder(User):
    """
    Defines a Bidder which is-a User, but can place bids on carpet
    instances.
    """
    def __init__(self, username, password):
        super().__init__(username, password)
        self.bids = [] # Contains carpet objects.
        self.won = []

    @property
    def active_bids(self):
        """
        Return list of bids which are still in stock.
        """

        bids = [bid for bid in self.bids if bid.in_stock]
        return bids

    def bid(self, carpet, amount):
        """
        Place a bid on carpet instance of 'amount', if bidder is not the
        most recent bidder of the carpet.
        """
        if carpet.bids_left > 0:
            try:
                carpet.add_bidder(self, amount)
                self.bids.append(carpet)

            except ValueError:
                print("Cannot place bid. Wait for another bidder to place bid!")

            else:
                print("Bid successfully placed!")

    def increase_bid(self, carpet, amount):
        """
        Increase the bid amount placed on carpet.

        carpet: Carpet instance on which a bid is already placed.
        """
        min = carpet.bidders.get(self, carpet.base_price)

        if min < amount:
            carpet.add_bidder(self, amount)

        else:
            raise ValueError(f"Bid cannot be smaller than {min}")

    def cancel_bid(self, carpet):
        """
        Cancel a bid placed on carpet, remove self from carpet's known bidders,
        increasing the bid count for the carpet.
        """
        self.bids.remove(carpet)
        carpet.bidders.remove(self)
        carpet.bids_left += 1

    def cancel_all_bids(self):
        """
        Cancel all active bids of the bidder.
        """
        for bid in self.active_bids:
            self.cancel_bid(bid)
