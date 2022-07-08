""""" 
class Shoe:
    def __init__(self):
        self.brand = "Vans"
        self.type = "Classic Sk8-Hi"
        self.price = 69.99
        self.in_stock = True 

skate_shoe = Shoe()
dress_shoe = Shoe()

skate_shoe.type = "High-top Trainers"
dress_shoe.type = "Ballet Flats"

print(skate_shoe.type)
print(dress_shoe.type)

"""
# class Shoe:
#     def __init__(self, brand, shoe_type, price):
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#         self.in_stock = True

# skate_shoe = Shoe("Vans", "High-top Trainers", 59.99)
# dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
# theo_shoe =  Shoe("Nike", "High-tops", 1000)

# print(skate_shoe.brand)
# print(dress_shoe.brand)
# print(theo_shoe.brand)

# Methods & Updating Attributes


class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True

    def on_sale_by_percent(self,percent):
        self.price = self.price * (1- percent)

    def total_plus_tax(self,tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total
    def cut_price(self,ammount):
        if ammount < self.price:
            self.price -= ammount
        else:
            print("Price deduction too large.")
    def add_price(self,amouunt):
        self.price += amouunt


skate_shoe = Shoe("Vans", "High-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
skate_shoe.on_sale_by_percent(0.2)
dress_shoe.on_sale_by_percent(0.5)
print(dress_shoe.price)

# print(skate_shoe.total_plus_tax(0.10))
skate_shoe.cut_price(20)
skate_shoe.add_price(10)
print(skate_shoe.price)
