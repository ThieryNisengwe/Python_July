'''Association Between Classes'''


class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = 0

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print("Insufficent Funds: Charging a $5 fee")
            self.balance -= 5
            return self
        # your code here

    def display_account_info(self):
        # your code here
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
        return self
        # your code here

    def print_info(self):
        self.display_account_info()
        print(f"Interest Rate:{self.int_rate}")
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)  # added this line


class User:
    def example_method(self):
        # we can call the BankAccount instance's methods
        self.account.deposit(100)
        # or access its attributes
        print(self.account.balance)
