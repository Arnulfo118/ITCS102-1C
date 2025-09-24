print("Multiplication Table Maker")
print("--------------------------")
num = eval(input("Enter a number to create its multiplication table: "))
for i in range(1,11,1):
    print(num, "x", i, "=", num*i)