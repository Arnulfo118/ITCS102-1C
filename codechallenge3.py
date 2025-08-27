name = input("What is your name?... ")
isStudent = input("Are you a student? (Y/N)... ")
farePrice = eval(input("How much will be your fare?... "))



if (isStudent == 'Y'):
	farePriceDiscount = farePrice * 0.2
	newFarePrice = farePrice - farePriceDiscount
	print("Hi", name + ", you are eligible for a discount of 20% off!")
	print("Your discount will be", int(farePriceDiscount),"pesos, making your new fare price to", int(newFarePrice),"pesos!")
else: 
		print("Hi", name + ", unforunately only students are eligible for a discount.")
		print("Regular fare of", farePrice,"still applies.")