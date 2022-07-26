#OOP- used to save time and use less code. 
# Attribuutes(Properties)- for a tree this would be (Trunk,Leaves,Branches)
#Methods-(Behaviors)- for a tree this would be(Growing,Producing Fruit and dropping leaves)
#this is the key for organization
#Instance/Objects-are the same thing.

#Classes-

#Constructor & Attributes

class User:
    def __init__(self):
        self.first_name = "Brandon"
        self.last_name = "Theo"
        self.age = 21
        self.height = '8ft'
        self.male = False 

print("The best President of all time is me!")

user_tony = User()
user_evan = User()
print(user_tony.first_name)
print(user_evan.first_name)

#Setting Attributes
class User:

    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


