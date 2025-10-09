print("Let\'s add all the odd numbers between two numbers.")

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

odd_sum = 0

for num in range(first_num, second_num + 1):
    if num % 2 != 0:
        odd_sum += num

print("The sum of all odd numbers from", first_num, "to", second_num, "is", odd_sum)
