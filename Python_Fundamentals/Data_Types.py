#Primitive data types
#The basic building blocks of a language(Boolean, Numbers, Strings)

#Boolean Values-True or False
from hashlib import new


is_huungry = True
has_freckles = False

#Numbers, whole numbers are int. decimal numbers are floats or complex numbers. 
age = 35
weight = 160.57

#Strings - Literally text
name = "Joe Blue"
name2= "Thiery"

#Composite Types - 
# Are collections of multiple primite types(Bollean's Numbers Strings)

#Tuples- A type of data that is immutable(Can't be changed or modified after it's made.)

dog = ('Bruce', 'cooker spaniel', 19, False)
print(dog[0])
# dog[1] = 'dachshund'

#Lists = A type of data that is mutable(Can be modified after it's creation) usually meant to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)
ninjas.pop() #pop removes last item in array. setting a [1] will remove item in array starting from last
print(ninjas)
ninjas.pop(1) #read pop 2 lines above
print(ninjas)

#Dictionaries A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values.
empty_dict = {}
new_person = {'name': 'Jhon', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)
w = new_person.pop('weight') #removes the specfied key('weight') and returns the value
print(w) 
print(new_person)

#Common Functions "if we're unsure of a value or varible's data type, we can use the type function to find out what it is."
print(type(2.63))
print(type(new_person))

#Numbers - there are 3 basic types of numbers in python 
#int- whole numbers, positive or negative. ex 69
#float - decimal numbers, positive or negative. ex 4.2
#complex- are a part of the real number system and are often refrenced with the ltter j ex 1 +3j. DON'T USE UNTIL YOU KNOW THIS ONE
#if you don't know which type a number is use the type() function.
print(type(24))
print(type(3.9))
print(type(3j))

#Conversion- All Python objects have data type methods we can use to conver nuumber types from one to another. (Turn Floats into Int's and Int's into Floats and Int's into Complex)

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

#Random Number - Python does not have a built in random number generator, use the random module instead. 

import random
print(random.randint(2,5)) #Should give us a random number between 2,5. "It works!"


