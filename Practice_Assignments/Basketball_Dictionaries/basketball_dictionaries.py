'''Basketball Dictionaries'''


# Students will update a class constructor to accept a single dictionary of data, rather than many arguments.
# Students will use dictionary data to create an object instance
# Students will populate a list of object instances from a list of dictionaries
# Students will write a class method that populates a list of object instances from a list of dictionarie

# 1. Assignment
# Paul is a fantasy basketball league manager, but also a programmer! He is trying to organize fantasy teams of players (that can be from any of the real teams) for his league website. There is already a web service that collects the line
# -up data from friends in batches.So far, he has been able to get a single list of dictionaries at a time from the API, and would like to put each team into a list of Player object instances, so that he can use methods related to players.
# The lists look something like this:

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

'''Challenge 1: Update the Constructor'''


class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team


kyrie = {"name": "Kyrie Irving", "age": 32,
         "position": "Point Gaurd", "team": "Los Angeles Lakers"}

player_kyrie = Player(kyrie['name'], kyrie['age'],
                      kyrie["position"], kyrie["team"])

print(player_kyrie.age)


'''Challenge 2: Create instances using individual player dictionaries.'''

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# Create your Player instances here!
# player_jason = ???

kevin_player = Player(kevin["age"], kevin["name"],
                      kevin["position"], kevin["team"])

'''Challenge 3: Make a list of Player instances from a list of dictionaries'''

# Finally, given the example list of players at the top of this module (the one with many players) write a
# for loop that will populate an empty list with Player objects from the original list of dictionaries.

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

new_team = []
# Write your for loop here to populate the new_team variable with Player objects.
    