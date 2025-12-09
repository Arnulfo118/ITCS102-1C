def greetname(name):
    print(f"Hello {name}!")

def greet(name, loc, age):
    print(f"Hi {name} from {loc}, {age} yr\'s old")

def funcwithReturn(number):
    print(f"The summation of all numbers from 1 to {number}")
    sum = 0
    for x in range(1, number + 1, 1):
        sum += x
    return sum


def fac(number):
    print(f"The factorial of all numbers from 1 to {number}")
    factorial = 1
    for x in range(1, number + 1, 1):
        factorial *= x
    return factorial
