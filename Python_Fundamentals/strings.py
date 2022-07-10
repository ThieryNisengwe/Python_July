print("this is a simple string")

name = "Zen"
print("My name is", name)

print("My name is " + name)


# print("Hello" + 42)
print("Hello " + str(42))

total = 35
user_val = "26"
# total = total + user_val
total = total + int(user_val)
print(total)

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name.upper} {last_name.upper} and I am {age} years old.")
# print(f"My name is {age} {first_name} and I am {last_name} years old.")

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
print(first_name)
print(first_name.upper())