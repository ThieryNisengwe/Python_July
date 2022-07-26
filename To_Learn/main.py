'''1. Iterate Through a List of Dictionaries'''
# This is a function that loops through the dictionary
# in the list and prints each key and the value it has.


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_list):
    for students in some_list:
        print(f"first_name - {students['first_name']}, last_name - {students['last_name']}")


iterateDictionary(students)


'''2. Iterate Through a List of Dictionaries'''
# the print(f"first_name-{cohorts['first_name']}, last_name - {cohorts['last_name']}")
# prints the first key and it's value and the last name and it's value. 

cohorts = [
    {'first_name': 'Raph', 'last_name': 'Tom'},
    {'first_name': 'Kelvin', 'last_name': 'Chan'},
    {'first_name': 'Kennia', 'last_name': 'Brandon'},
    {'first_name': 'Henrik', 'last_name': 'Connor'},
]

def gothroughlist(anything):
    for cohorts in anything:
        print(f"first_name - {cohorts['first_name']}, last_name - {cohorts['last_name']}")

gothroughlist(cohorts)

'''3. Get Values From a List of Dictionaries'''
# create a function that will print the value stored in each key

def printvalue(key_name,a_list):
    for cohort in a_list:
        print(cohort[key_name])

printvalue('first_name',cohorts)
printvalue('last_name',cohorts)

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each
# key along with the size of its list, and then prints the associated values within each key's list. For example:

def printInfo(some_dict):
    print(len(some_dict['locations']), "LOCATIONS")
    for location in some_dict['locations']:
        print(location)
    print()
    print(len(some_dict['instructors']), "INSTRUCTORS")
    for location in some_dict['instructors']:
        print(location)


seattle = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(seattle)