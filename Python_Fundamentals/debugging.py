# # # # # def multiply(num_list, num):
# # # # #     for x in num_list:
# # # # #         x *= num
# # # # #     return num_list
# # # # # a = [2,4,10,16]
# # # # # b = multiply(a,5)
# # # # # print(b)
# # # # # # output:
# # # # # # >>>[2,4,10,16]

# # def multiply(num_list, num):  # don't go inside the function until the function is called
# #     a = [2, 4, 10, 16]
# #     # now our function executes; what is a function call equal to?
# #     b = multiply(a, 5)
# #     print(b)  # and the resulting value is printed


# # def multiply(num_list, num):
# #     print(num_list, num)
# #     for x in num_list:
# #         x *= num
# #     return num_list
# # a = [2,4,10,16]
# # b = multiply(a,5)
# # print(b)
# # # output:
# # # >>>[2,4,10,16] 5
# # # >>>[2,4,10,16]

# # def multiply(num_list,num):
# #     print(num_list, num)
# #     for x in num_list:
# #         print(x)
# #         x *= num
# #     return num_list
# # a = [2,4,10,16]
# # b = multiply(a,5)
# # print(b)
# # # output:
# # # >>>[2, 4, 10, 16] 5
# # # >>>2
# # # >>>4
# # # >>>10
# # # >>>16
# # # >>>[2, 4, 10, 16]

# # def multiply(num_list, num,):
# #     print(num_list, num,)  # output should be [2,4,10,16] 5
# #     for L in num_list:
# #         # print(L)
# #         L *= num
# #         print(L)

# #     return num_list
# # a = [2, 4, 10, 16]
# # b = multiply(a, 5,)
# # print(b)
# # output:
# # >>>[2,4,10,16] 5
# # >>>2
# # >>>10
# # >>>4
# # >>>20
# # >>>10
# # >>>50
# # >>>16
# # >>>80
# # >>>[2, 4, 10, 16]


# # output:
# # >>>[2, 4, 10, 16] 5
# # >>>2
# # >>>4
# # >>>10
# # >>>16
# # >>>[2, 4, 10, 16]

# # def divide(num_list,num):
# #     print(num_list,num)
# #     for y in num_list:
# #         print(y)
# #         y *=num
# #         return num_list

# def multiply(num_list,num):
#     print(num_list, num) # output should be [2,4,10,16] 5
#     for x in num_list:
#         print(x)
#         x *= num
#         print(x)
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)


def multiply(num_list, num):
    print(num_list, num)  # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(num_list)
    return num_list


a = [2, 4, 10, 16]
b = multiply(a, 5)
print(b)

def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[10,20,50,80]

