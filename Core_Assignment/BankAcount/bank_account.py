'''1. Assignment: BankAccount'''
# Students will follow specifications for creating a class.
# Students will implement default arguments in parameters for attributes that can be assigned on instantiation.
# Students will use basic programmatic logic to implement the functionality of a bank account
# Students will handle edge-cases, such as insufficient funds, with the appropriate control structure (if-else, code flow, or early exit)
# Students will demonstrate proficiency in creating and update attributes of an object instance, from within the class using self .
# Students will thoroughly test the functionality of their class by creating instances and calling methods with different test data and scenarios.

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
        if  self.balance > 0:
            self.balance *= self.int_rate
        return self
        # your code here
    def print_info(self):
        self.display_account_info()
        print(f"Interest Rate:{self.int_rate}")
        return self

thiery_account = BankAccount(0.01,0)
tom_account = BankAccount(0.03,0)

thiery_account.deposit(100).deposit(300).deposit(100).yield_interest().display_account_info().display_account_info().print_info()
tom_account .deposit(200).deposit(200).withdraw(100).withdraw(50).withdraw(50).withdraw(100).display_account_info().print_info()