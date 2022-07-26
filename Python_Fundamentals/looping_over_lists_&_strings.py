# # # for x in 'Hello':
# # #     print(x),
# # # # output: 'H', 'e', 'l', 'l', 'o'


# my_list = ["abc", 123, "xyz"]
# for i in range(0, len(my_list)):
#     print(i, my_list[i])
# # output: 0 abc, 1 123, 2 xyz

# # OR

# for v in my_list:
#     print(v)
# # output: abc, 123, xyz


# # countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# # # Challenge 1: Fix the range!
# # for integer in range(0, len(countries)):
# #     print("Index:")
# #     # Challenge 2: print the index here
# #     print("Country:")
# #     # Challenge 3: print the country here

# # # Looping over values only...
# # for country in countries:
# #     print("Country: ")
# #     # Challenge 4: print the country here
# for count in range(0, 5):
#     print("looping =", count)

# count = 0
# while count <= 5:
#     print("looping = ", count)
#     count += 1

# while < expression >:
# do something, including progress towards making the expression False. Otherwise we'll never get out of here!

# count = 0
# while count <= 5:
#     print("looping =", count)
#     count += 1

# numbers = 0
# while numbers <= 10:
#     print("looping", numbers)
#     numbers += 1

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")

# y = 0
# while y < 10:
#     print(y)
#     y = y+1
# else:
#     print("We got to 10!")

# y = 10
# while y > 0:
#     print(y)
#     y = y-1
# else:
#     print("We got to 0!")

# for val in "string":
#     if val == "i":
#         break
#     print(val)
# # output: s, t, r

# for val in "string":
#     if val == "r":
#         continue
#     print(val)
# # output: s, t, r, n, g
# # notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1

