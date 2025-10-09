factor = 1
a = eval(input("Enter your number: "))

for i in range (a, 0, -1):
    factor *= i 

print("The factorial of", a, "is", factor)