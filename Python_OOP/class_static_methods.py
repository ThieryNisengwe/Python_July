# # class BankAccount:
# #     pass
#     # Declaring a class attribute
#     # Shared among all bank accounts
#     # bank_name = "First National Dojo"

#     # def __init__(self, int_rate, balance):
#         # self.int_rate = int_rate
#         # self.balance = balance
#         # pass

# # adriensAccount = BankAccount(0.01,200)
# # sadiesAccount = BankAccount(0.01,400)
# # adriensAccount.bank_name = "Dojo Credit Union"
# # sadiesAccount.bank_name = "Thiery's Bank"

# # print(adriensAccount.bank_name)
# # output: Dojo Credit Union

# # print(sadiesAccount.bank_name)
# # output: First National Dojo

# # BankAccount.bank_name = "Bank of Dojo"

# # print(adriensAccount.bank_name)
# # output: Bank of Dojo

# # print(sadiesAccount.bank_name)
# # output: Bank of Dojo

# class BankAccount:
#     # class attributes
#     bank_name = "First National Dojo"
#     # new class attribute - a list of all the accounts!
#     all_accounts = []

#     def __init__(self, int_rate,balance):
#         self.int_rate = int_rate
#         self.balance = balance
#         BankAccount.all_accounts.append(self)
#     # class method to change the name of the bank
#     @classmethod
#     def change_bank_name(cls,name):
#         cls.bank_name = name
#     # class method to get balance of all accounts
#     @classmethod
#     def all_balances(cls):
#         sum = 0
#         # we use cls to refer to the class
#         for account in cls.all_accounts:
#             sum += account.balance
#         return sum

# BankAccount.change_bank_name("New Bank")
# BankAccount.all_balances()
# Tony = BankAccount(0,200)
# print(BankAccount.bank_name)
# Thiery = BankAccount.change_bank_name("Thiery's Bank")
# BankAccount.all_balances()
# Theiry = BankAccount(0.1,100)
# print(BankAccount.all_balances())

class BankAccount:
    # ... __init__ goes here
    def __init__(self,balance):
        self.balance = balance
    def with_draw(self, amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self.balance
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod

    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
    
    def can_deposit(self, amount):
        self.balance +=amount 
        return self.balance


Thiery = BankAccount(500)
print(Thiery.can_deposit(500))
print(Thiery.with_draw(100))
