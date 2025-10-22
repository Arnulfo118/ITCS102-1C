import random

print("Guess the number between 1 and 10")
print("You have 3 attempts to guess the correct number.")
print("-" * 30)
number_to_guess = random.randint(1, 10)
number_of_attempts = 0
guessing = True

name = input("Enter your name: ")

while guessing:
    user_guess = eval(input("Enter your guess: "))
    number_of_attempts += 1

    if user_guess == number_to_guess:
        print(f"Congratulations {name}! You've guessed the correct number {number_to_guess} in {number_of_attempts} attempts.")
        guessing = False
    elif user_guess < number_to_guess:
        print("Your guess is too low. Try again.")
    elif number_of_attempts >= 3:
        print(f"Sorry {name}, you've used all your attempts. The correct number was {number_to_guess}.")
        guessing = False
    else:
        print("Your guess is too high. Try again.")