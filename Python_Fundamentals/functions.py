# # # def add(a, b):  # function name: 'add', parameters: a and b
# # #     x = a + b  # process
# # #     return x  # return value: x


# # # new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
# # # the result of the add function gets sent back to and saved into new_val, so we will see 8
# # # print(new_val)

# # # new_val2 = add(10, 20)
# # # print(new_val2)


# # # def say_hi(name):
# # #     print("Hi, " + name)


# # # say_hi('Thiery')
# # # say_hi('Alfred')
# # # say_hi('William')

# # def say_hi(name):
# #     return "Hi " + name


# # # the returned value from say_hi function gets assigned to the 'greeting' variable
# # greeting = say_hi("Kobe")
# # print(greeting)  # this will output 'Hi Michael'


# # def say_bye(name):
# #     return "Bye " + name


# # farewell = say_bye('LeBRON')
# # print(farewell)

# def add(a, b):
#     x = a + b
#     return x
# sum1 = add(4,6)
# sum2 = add(1,4)
# sum3 = sum1 + sum2

# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

def full_name(first_name, last_name):
    full_name = (first_name + last_name)
    return full_name
    # your code here!


name1 = full_name("Eddie ", "Brock")
print(name1)  # should print Eddie Aikau

# Challenge 2:
#   Call the function again using your own name and print the results!
name2 = full_name("Thiery ", "Nis")
print(name2)

name3 = full_name("Yuriy", " Martyn")
print(name3)

name4 = full_name("Foday", " Konneh")
print(name4)
