name = input("Enter your name: ")

print("+" * 30)
print("ODD or EVEN Number Checker")
print("+" * 30)

isNotZero = True
odd_list = []
odd_sum = 0

while isNotZero:
    num = eval(input("Enter a number (0 to exit): "))
    if num == 0:
        isNotZero = False
        print(f"\n\n{name}, you have exited the program.")
        print("-" * 30)
        print(f"The sum of all ODD numbers which is {odd_list} is: {odd_sum}")
        print("-" * 30)
    elif num % 2 == 1:
        print(f"{num} is an ODD number.")
        odd_list.append(num)
        odd_sum += num
    else:
        print(f"{num} is an EVEN number.")
    continue