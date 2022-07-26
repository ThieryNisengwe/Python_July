def add(num1,num2):
    x = num1+num2
    print(x)
    return x

print(add(2,3))

def add_three(num1,num2=3):
    return num1 + num2

print(add_three(5))

print(add_three(8,4))
