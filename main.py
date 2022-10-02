class Wallet:
    def __init__(self, money = 0):
        self.money = money
        
    def credit(self, amount):
        self.amount = amount
        self.money += amount
        print(f"You now have {self.money} KWD in your wallet.")

    def debit(self, amount):
        self.amount = amount
        self.money -= amount
        print(f"You now have {self.money} KWD in your wallet.")

    def __str__(self):
        return f"You have {self.money} KWD in your wallet."


class Person:
    def __init__(self, name, location, wallet):
        self.name = name
        self.location = location
        self.wallet = Wallet(wallet)

    def moveTo(self, point):
        self.point = point
        self.location = point
        print(f"{self.name}'s new location is now {self.location}.")
    
    def __str__(self):
        return f"You're name is {self.name}, you're location is {self.location}. {self.wallet}"


class Vendor(Person):
    def __init__(self, name, location, wallet, range = 5, price = 1):
        super().__init__(name, location, wallet)
        self.range = range
        self.price = price

    def sellTo(self, customer, number_of_icecreams):
        self.moveTo(customer.location)
        self.wallet.credit(self.price * number_of_icecreams)
        customer.wallet.debit(self.price * number_of_icecreams)
        print(f"{number_of_icecreams} ice creams were sold!")

    def __str__(self):
        return f"You are the vendor. {super().__str__()} Your range is {self.range} and your price per ice cream is {self.price} KWD."


class Customer(Person):
    def __init__(self, name, location, wallet):
        super().__init__(name, location, wallet)

    def _is_in_range(self, vendor):
        if abs(self.location - vendor.location) <= vendor.range:
            print("The customer is in range!")
            return True
        else:
            print("The customer is out of range.")
        return False
    
    def _have_enough_money(self, vendor, number_of_icecreams):
        if self.wallet.money >= (vendor.price * number_of_icecreams):
            print("The customer has enough money for this purchase!")
            return True
        else:
            print("The customer does not have enough money for this purchase.")
        return False

    def request_icecream(self, vendor, number_of_icecreams):
        if self._is_in_range(vendor) and self._have_enough_money(vendor, number_of_icecreams):
            print("A request has been made to the vendor!")
            vendor.sellTo(customer, number_of_icecreams)

    def __str__(self):
        return f"You are the customer. {super().__str__()}"



vendor = Vendor("Ahmed", 5, 100)
customer = Customer("May", 10, 10)
customer.request_icecream(vendor, 10)

