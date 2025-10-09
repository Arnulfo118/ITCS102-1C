temp = eval(input("Enter a number: "))

if temp == 0:
    print("Temperatur is at the freezing point.")
elif temp >=1 and temp <= 20:
    print("Temperature is very cold.")
elif temp >=21 and temp <= 30:
    print("Temperature is cold.")
elif temp >=31 and temp <= 37:
    print("Temperature is normal.")
elif temp >=38 and temp <= 45:
    print("Temperature is hot.")
elif temp >=46 and temp <= 60:
    print("Temperature is boiling hot.")
elif temp > 60:
    print("Temperature is at the burning point.")
else:
    print("Invalid input.")