'''OOP & Dictionaries Practice'''


# Students will be able to articulate the similarities and differences between dictionaries and OOP classes
# Students will set instance attributes to values from a dictionary.
# Students will be able to explain why manipulating key-value pair structures is important in programming
# Students will recall from memory some of the names for key-value pair structures in different languages.

# 1. Key-Value Pair Data Structures
# Yes, we're going to take a minute to talk about dictionaries again. In this course, particularly when you get to Flask, you will be handling dictionaries A LOT. By the end, hopefully you'll have
# a very good feel for working with dictionaries, debugging key-value errors, and parsing dictionaries in conjunction with OOP classes. So other than Flask, why are we emphasizing dictionaries?

# 2. Common Format for Data-Interchange
# Something you will see ubiquitously as a programmer is that key-value pair structures are often used for data coming from other sources, even from external programs written in different languages, typically in the form of JSON through an API, 
# which can be parsed by Python into dictionaries. You'll learn more about APIs later, but another more urgent reason you need to use them is because when we get to our Flask framework, this is how you'll receive information from the database!

# 3. Comparing Dictionaries to OOP Classes

# What are some ways in which OOP Classes are similar to dictionaries?

# Dictionaries Have unique keys for stored values. Have access to many pieces of data through a single dictionary. using a key.
# OOP Class Have unique attribute names for stored values. Have access to many attribute values through a single object instance using an attribute name. 

# What are some differences, limitations and advantages of each?
# Dictionaries Can add new-key value pairs to an existing dictionary. This is flexible, but doesn't suit data that should be uniform(stay the same). Can store functions, but does not inherently sahre these functions with other dictionaries. 
# OOP Classes Generally cannot add new attributes to an exisiting obeject instance. Keeps data uniform, but has little capacity for non-uniform data. A class can have instance methods that are shared across all instances. 

'''Making Object Instances from Dictionary Data'''

# Consider the following dictionary:

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
    
# Pass in all the values from the dictionary by their keys
player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.position) # prints small forward

'''Update the Constructor!'''

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Uncomment the line below to test
player_kevin = Player(kevin["name"],kevin["age"],kevin["position"],kevin['team'])
print(player_kevin.position)


# Let's say you were receiving data from an external source like a data base, and wanted to turn this diction data into a Player object so you could write some useful
# Methods associated with players. youu can imagine just from the way the dictionary is structured that you might write your class like this: 

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

# Okay, now that we have a class defined, let's take our dictionary info to make a Player instance.

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
        
# kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
# Uncomment the line below to test
player_kevin = Player("Kevin","33","Small Foward","Suns")

print(player_kevin.name)
print(player_kevin.age)
print(player_kevin.position)
print(player_kevin.team)

'''Other Fun Facts About Dictionaries'''
# They're fast
# Almost every language has a built-in key-value pair data structure.
