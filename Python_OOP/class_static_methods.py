'''1. Class vs Instance'''

# We're now accustomed to designating instance attributes inside the constructor, the __init__() method. However, we can also declare and set attributes that don't belong to a single instance but to the class itself. Likewise, normally when we create a method
# on a class we pass in self to refer to the instance of the object.  These normal methods are referred to as instance methods.  But there are other types of methods we can implement on the class.  Methods that belong to the class and not the instance.

# 1. Class Attributes 

# Class attributes are defined outside of any instance methods, and is shared among all instances of the class.  
# Class attributes are more flexible because we can change them on an instance or the entire class.

class BankAccount:
    # Declaring a class attribute
    # Shared among all bank accounts 
    bank_name = "First National Dojo"		
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

# Changing them on an instance:  

adriensAccount = BankAccount(0.1,250)
sadiesAccount = BankAccount(0.01,300)
adriensAccount.bank_name = "Dojo Credit Union"
    
print(adriensAccount.bank_name)
# output: Dojo Credit Union
    
print(sadiesAccount.bank_name)
# output: First National Dojo


BankAccount.bank_name = "Bank of Dojo"

print(adriensAccount.bank_name)
# output: Bank of Dojo

print(sadiesAccount.bank_name)
# output: Bank of Dojo

'''2. @classmethod'''
# Class methods are defined with a decorator @classmethod. They belong to the class itself instead of the instance.
# Instead of implicitly passing self into the method, we pass cls. This is reference to the class.

# This is how we write @classmethods:

class BankAccount:
    # class attributes
    bank_name = "First National Dojo"
    # new class attribute - a list of all the accounts!
    all_accounts = []

    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum

BankAccount.change_bank_name("New Bank")
Tony = BankAccount(0,200)
Thiery = BankAccount.change_bank_name("Thiery's Bank")
print(BankAccount.bank_name)
Theiry = BankAccount(0.1,100)
print(BankAccount.all_balances())

'''3. @staticmethod'''

# Static methods are functions defined within the class with a decorator @staticmethod.  They have no access 
# on instance or class attributes, so if we need any existing values, they need to be passed in as arguments.

# If we wanted our BankAccount class to have a utility function to add or subtract we could implement @staticmethod on the class.

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

# In Python, static methods offer us the opportunity to organize our code in a better way. We could do a simple check
# to see if the account can be withdrawn from, but what if we want to scale up our application with more 
# logic around this idea? Well then we would have to update everywhere we are making that evaluation, but if we put
# it in a @staticmethod, then we can update all the checks from one place. And our code becomes a bit more D.R.Y.

#Reflection Questions 

# How would you describe the difference between static and class methods, in your own words?
# If you start to get stuck in OOP, what strategies and resources would you turn to for help?

# Class methods belong to the class itself instead of the instance. where as static methods are functions defind within the class.
# they have no access on instance or class attributes, so if you need exisiting values they need to be passed in as arguments. 

#cohorts Ta's and then instructors if needed. 