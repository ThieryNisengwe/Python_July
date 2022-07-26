"""Messed around with the code to get an understanding of it. """
# for i in range(151):
#     print(i)

# for i in range(5, 1000, 5):
#     print(i)

# for i in range(1, 101):
#     if i % 5 == 0:
#         print("Coding")
#     if i % 10 == 0:
#         print("Dojo")
#     else:
#         print(i)

# totalsum = 0
# for num in range(0, 500000):
#     if num % 2 != 0:
#         totalsum += num
# print("The Sum of ood numbers is :", totalsum)


# def count_down_four():
#     number = 2018
#     while number > 0:
#         print(number)
#         number = number - 4


# count_down_four()


# def flex_downcounter(low, high, mult):
#     for i in range(low, high+1):
#         if i % mult == 0:
#             print(i)


# flex_downcounter(2, 9, 3)


# for x in range(0, 151):
#     print(x)

# for i in range(5, 1001, 5):
#     print(i)

# for y in range(1, 101):
#     print(y)
# if

# for y in range(0,101):
#     if y % 5 == 0:
#         print("Coding")
#     if y % 10 == 0:
#         print("Coding Dojo")
#     else:
#         print(y)


# max = int(input("Please Enter the Max Value"))
# total = 0

# for number in range(1, max+1):
#     if(number % 2 == 0):
#         print("{0}".format(number))
#         total = total + number
# print("The sum of Even Numbers from 1 to {0} = {1}".format(number, total))

# max1 = int(input("Please Enter the Max"))
# total1 = 0
# for number in range(1, max1+1):
#     print(f"{0} {number}")
#     total = total1 + number
# print(f"The sum of Even Numbers from 1 {0} = {1}{number} {total1}")


# maximum = int(input("Please Enter the Maximum Value:"))
# Oddtotal = 0
# for number in range(1,maximum+1):
#     if(number % 2 != 0):
#         print("{0}".format(number))
#         Oddtotal = Oddtotal + number
# print("The sum of Odd Numbers from 1 to {0} = {1}".format(number,Oddtotal))

# print("62500000000")

# y = 10
# while y > 0:
#     print(y)
#     y = y-1
# else:
#     print("We got to 0!")

# y = 2018
# while y > 0:
#     print(y)
#     y -= 4

# lowNum = 1

# highNum = 10

# mult = 3

# print(lowNum), print(highNum), print(mult)

# def flex_downcounter(low, high, mult):
#     for i in range(low, high+1):
#         if i % mult == 0:
#             print(i)


# flex_downcounter(2, 9, 3)

def flexdown(low, high, mult):
    for y in range(low, high+1):
        if y % mult == 0:
            print(y)


flexdown(10, 100, 10)
