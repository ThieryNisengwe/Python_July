
for i in range(151):
    print(i)

for i in range(5, 1000, 5):
    print(i)

for i in range(1, 101):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Dojo")
    else:
        print(i)

totalsum = 0
for num in range(0, 500000):
    if num % 2 != 0:
        totalsum += num
print("The Sum of ood numbers is :", totalsum)


def count_down_four():
    number = 2018
    while number > 0:
        print(number)
        number = number - 4


count_down_four()


def flex_downcounter(low, high, mult):
    for i in range(low, high+1):
        if i % mult == 0:
            print(i)


flex_downcounter(2, 9, 3)
