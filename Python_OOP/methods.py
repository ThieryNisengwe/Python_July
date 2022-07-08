#OOP- used to save time and use less code. 
# Attribuutes(Properties)- for a tree this would be (Trunk,Leaves,Branches)
#Methods-(Behaviors)- for a tree this would be(Growing,Producing Fruit and dropping leaves)
#this is the key for organization
#Instance/Objects-are the same thing.

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    # adding a greeting method
    def greeting(self):
        print(f"Hello, my name is {self.name}")

adrien = User("Adrien", "adion@codingdojo.com")
cool_person = User("Sadie", "sflick@codingdojo.com")

adrien.greeting()
cool_person.greeting()

#Methods & Updating Attributes
