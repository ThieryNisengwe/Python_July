from dis import dis


class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def widthdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds!")
            return self
        self.balance = self.balance - amount
        print(self.balance)
        return self

    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self

    def yeild_interest(self):
        self.balance += self.balance * self.int_rate
        return self


Conner = BankAccount(.9, 100)
Conner.deposit(0).display_account_info().deposit(1000000).widthdraw(1000000).deposit(10000).yeild_interest().display_account_info()

Thiery = BankAccount(.9, 100)
Thiery.widthdraw(0).display_account_info().widthdraw(1000000).widthdraw(1000000).widthdraw(10000).yeild_interest().display_account_info()



