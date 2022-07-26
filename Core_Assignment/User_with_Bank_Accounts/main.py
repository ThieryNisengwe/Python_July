'''Users with Bank Accounts'''

class BankAcount:
    def __init__(self, int_rate, balance, balance_2):
        self.int_rate = int_rate
        self.balance = 0
        self.balance_2 = 0

    def deposit(self, amount, account,):
        if account == "Checkings":
            self.balance += amount
        elif account == "Savings":
            self.balance_2 += amount
        return self

    def withdraw(self, amount, account):
        if account == "Checkings":
            if self.balance >= amount:
                self.balance -= amount
                return self
            else:
                print("Insufficent Funds: Charging a $5 fee")
                self.balance -= 5
                return self
        if account == "Savings":
            if self.balance_2:
                self.balance_2 -= amount
                return self
            else:
                print("Insufficent Funds: Charging a $5 fee")
                self.balance_2 -= 5
                return self

    def display_account_info(self):
        print(f"Checkings: {self.balance}")
        print(f"Savings: ${self.balance_2}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate + self.balance)
            return self
        return self

    def print_info(self):
        self.display_account_info()
        print(f"Interest Rate: {self.int_rate}")


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAcount(int_rate=0.04, balance=0, balance_2=0)
        self.other_user = BankAcount(int_rate=0.08, balance=0, balance_2=0)
    def display_user_balance(self):
        self.account.display_account_info()

    def make_deposit(self, amount,account):
        self.account.deposit(amount,account)
        return self
    
    def make_withdrawl(self,amount,account):
        self.account.withdraw(amount,account)
        return self 
    
    def transfer_money(self,amount,other_user):
        self.account.withdraw(amount,"Checkings")
        self.other_user.deposit(amount,"Checkings")

user_1 = User("Thiery,","thierynisengwe@gmail.com")
user_2 = User("Ralph", "Ralph@gmail.com")
user_1.make_deposit(300,"Checkings").make_deposit(600,"Savings").make_withdrawl(0,"Savings").make_withdrawl(0,"Checkings").display_user_balance()
user_2.display_user_balance()