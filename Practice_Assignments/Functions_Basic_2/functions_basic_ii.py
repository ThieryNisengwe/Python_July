
# def count_down(num):
#     new_list = []
#     for i in range(num, -1, -1):
#         new_list.append(i)
#     return new_list


# print(count_down(5))


# def print_return(list):
#     print(list[0])
#     return list[1]


# print(print_return([7, 21]))

# def first_plus_length(list):
#     print(list[0])
#     return len(list)
# print(first_plus_length([42,10,68]))

# def val_greater_sec(list):
#     if len(list) < 2:
#         return False
#     new_list = []
#     for val in list:
#         if val > list[1]:
#             new_list.append(val)
#     print(len(new_list))
#     return new_list


# # print(val_greater_sec([]))
# print(val_greater_sec([4, -1, 5, 5]))
# print(val_greater_sec([5, 2, 3, 2, 1, 4, 3]))

#write a function that takes two integers as paratmers size and value the funtion should create and retun a list whose length is equal to the given size and who's values are all the given values.

def len_and_val(size,value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list
print(len_and_val(5,10))