name = input("What is your name?: ")
age = input("How old are you?: ")
fare = eval(input("How much is your fare?: "))
student= input("Are you a student? Y or N: ")


if student.lower() == "yes" or student.lower() == "y":
	discount = fare * 0.2
	newfare = fare - discount
	print("Hello,", name , ", you are eligible for discount", int(discount))
	print("Your new fare is", int(newfare))
else:
	print("Hello,", name , ", you are not eligible for discount")