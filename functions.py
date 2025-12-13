import time
import os
import msvcrt  # Windows-only

def wait_for_space(prompt="\nPress SPACE to continue..."):
    print(prompt, end="", flush=True)
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b' ':  # SPACE key
                print()  # move to next line
                return
        time.sleep(0.01)

def typewriter_print(message, delay=0.02, end="\n"):
    i = 0
    length = len(message)
    skip = False

    while i < length:
        # Detect space press
        if msvcrt.kbhit():
            if msvcrt.getch() == b' ':  # SPACE key
                skip = True

        if skip:
            # skip printing delay
            print(message[i:], end='', flush=True)
            break

        char = message[i]
        print(char, end='', flush=True)
        time.sleep(delay)

        # Natural pauses
        if char in ",;":
            time.sleep(delay * 10)
        elif char in ".!?":
            time.sleep(delay * 20)

        i += 1

    print(end=end, flush=True)

def basic_print():
    os.system('cls')
    typewriter_print("This is a basic print function.")
    typewriter_print("Using print() to display messages in Python.")
    typewriter_print("You have to put the messages inside the parentheses.")
    typewriter_print("Each message should be enclosed in quotes or you can use variables to display their values.")
    typewriter_print("\nYou can also separate multiple messages with commas like this: print('Hello,', 'world!')")
    typewriter_print("This will print: Hello, world!")

    typewriter_print("\nTry it out yourself!")
    user_message = input("\nType a message to print: ")
    typewriter_print("You typed:\n\n" + user_message)
    typewriter_print("You printed your message using the print() function in Python. Great job!")
    typewriter_print("\nThe code for this function is: \nprint('Your message here'). You can replace 'Your message here' with any message you want to print.")
    typewriter_print("That's how the basic print function works in Python!")

    wait_for_space()

def advanced_print():
    os.system('cls')
    typewriter_print("Hello\\nWorld!, this is an advanced print function. It uses \\n to create a new line. Printing:")
    typewriter_print("\nHello\nWorld!")
    typewriter_print("\nYou can also use special characters like \\t for tab spacing. For example:")
    typewriter_print("\nItem 1:\\tApple\nItem 2:\\tBanana\nItem 3:\\tCherry")
    typewriter_print("\nIt will print:\n\nItem 1:\t\tApple\nItem 2:\t\tBanana\nItem 3:\t\tCherry")
    typewriter_print("\nTry it out yourself!")
    user_message = input("\nType a message with \\n or \\t to see the effect: ")
    # Convert \n, \t, etc into real escape sequences
    user_message = user_message.encode().decode("unicode_escape")
    typewriter_print("You typed:")
    typewriter_print(user_message)
    typewriter_print("\nThat's how the advanced print function works in Python with special characters!")

    wait_for_space()

def input_function():
    os.system('cls')
    typewriter_print("This is an input function. It allows you to get input from the user and get the length of the input.")
    typewriter_print("\nFor example, let's ask for your name:")
    typewriter_print("Please enter your name:")
    name = input()
    typewriter_print("\nWelcome to the matrix, " + name)
    typewriter_print("Your name has " + str(len(name)) + " characters.")

    typewriter_print("""\nThe code for this function is:
                     
name = input("Type your name ---> ")
print("Welcome to the matrix,", name)
print("Your name has", len(name), "characters.")
                     
                    """)
    
    typewriter_print("\nThat's how the input function works in Python!")
    wait_for_space()

def eval_function():
    os.system('cls')
    typewriter_print("This is an eval function. It evaluates the value inside the parentheses. It will detect the value type and return the value accordingly.")
    typewriter_print("\nFor example, let's evaluate a mathematical expression:")
    typewriter_print("eval('3 + 5 * 2') will return:\n")
    result = eval('3 + 5 * 2\n')
    typewriter_print(str(result))
    print("\nYou can also evaluate strings, lists, and other data types using eval().")
    typewriter_print("\nFor example, eval('[1, 2, 3]') will return:\n")
    list_result = eval('[1, 2, 3]\n')
    typewriter_print(str(list_result))
    typewriter_print("Using type() function, we can check the data type of the evaluated result.")
    typewriter_print("type(eval('[1, 2, 3]')) will return:\n")
    typewriter_print(str(type(list_result)))

    typewriter_print("\nTry it out yourself!")
    while True:
        user_input = input("\nType a number: ")
        try:
            data_type = float(user_input) if "." in user_input else int(user_input)
            break
        except ValueError:
            print("\nStrings doesn't work in eval(), Enter something else like a float!")

    typewriter_print(f"The data type is a {str(type(data_type))}")
    typewriter_print(f"The value is {str(data_type)}")

    typewriter_print("\nThe eval() function can be very powerful but also dangerous if used with untrusted input. Always be cautious when using eval().")

    wait_for_space()

def equationals():
    os.system('cls')
    typewriter_print("Let's perform some basic arithmetic operations using eval() to get user input.")
    typewriter_print("There are several equational operations we can perform: addition (+), subtraction (-), multiplication (*), division (/), exponentiation (**), modulus (%), and floor division (//).")
    typewriter_print("\nPlease enter two numbers to perform these operations:")
    n1 = eval(input("Enter the first number.. "))
    n2 = eval(input("Enter the second number.. "))

    s = n1 + n2
    q = n1 - n2
    p = n1 * n2
    r = n1 / n2

    typewriter_print(f"\nThe sum of {n1} and {n2} is {s}.")
    typewriter_print(f"The difference of {n1} and {n2} is {q}.")
    typewriter_print(f"The product of {n1} and {n2} is {p}.")
    typewriter_print(f"The quotient of {n1} and {n2} is {r}.")
    typewriter_print(f"{n1} exponent by {n2} is {n1**n2}.")
    typewriter_print(f"The remainder of {n1} and {n2} is {n1%n2}.")
    typewriter_print(f"The floor division of {n1} and {n2} is {n1//n2}.")
    
    typewriter_print("""The equations used in this function are: 

s = n1 + n2
q = n1 - n2
p = n1 * n2
r = n1 / n2
                     
n1 being the first number and n2 being the second number.""")

    wait_for_space()
    
def augmented_assignment():
    os.system('cls')
    typewriter_print("This function demonstrates augmented assignment operators in Python.")
    typewriter_print("Augmented assignment operators allow you to perform an operation and assign the result back to the same variable in a more concise way.\n")
    typewriter_print("For example, instead of doing x = x + 1, you can do x += 1, this way you can update the variable without redundant variables.")

    typewriter_print("""Take this code block for example:
a = 10

print("The value of a is", a)

a += 5

print("The value of a is", a)

a += 5
a += 13
a -= 1
a *= 50
a **= 2


print("The value of a is", a)""")
    typewriter_print("It will print the following:\n")

    a = 10

    typewriter_print(f"The value of a is {a}")

    a += 5

    typewriter_print(f"The value of a is now {a}")

    typewriter_print("""\nWe will now do the following:
                        
a += 5
a += 13
a -= 1
a *= 50
a **= 2\n""")

    a += 5
    a += 13
    a -= 1
    a *= 50
    a **= 2


    typewriter_print(f"The value of a is now {a}")
    wait_for_space()

def string_concatenation():
    os.system('cls')
    typewriter_print("Let's learn about connecting two values from two variables.")
    typewriter_print("""Let's define two names.
For example:
                     
name1= 'Arnulfo'
name2= 'Fernandez'

Now, to connect these two names, we can use the '+' operator.
                     
name1 += name2 will result in 'ArnulfoFernandez' without a space. However, to add a space between the two names, we can do the following:
                     
name1 + ' ' + name2.""")
    
    typewriter_print("\nThis will result in the following full name:\n")
    name1= 'Arnulfo'
    name2= 'Fernandez'
    full_name = name1 + ' ' + name2
    typewriter_print(full_name)

    typewriter_print("This is called string concatenation.")

    typewriter_print("\nYou can also use this method to connect variables together using the '+' operator.")
    typewriter_print("Try it out yourself!")

    userfirst = input("\nType your first name: ")
    userlast = input("Type your last name: ")
    userfull = userfirst + ' ' + userlast
    typewriter_print("\nYour full name is: " + userfull)
    wait_for_space()

def if_match():
    os.system('cls')
    typewriter_print("Let's learn about conditional statements using if and else. Let's try to compare strings.")
    typewriter_print("\nFor example, let's do a simple username and password check.")
    typewriter_print("""Let's use this code block:
                     
username = input('Enter username.. ')
password = input('Enter password.. ')

if (username == 'User') and (password == 'user123'):
    print("User Logged in")
    print( (username == 'User') and (password == 'user123') )
else:
    print("Wrong credentials")

This code checks if the entered username and password match the predefined values. If they do, it prints 'User Logged in'; otherwise, it prints 'Wrong credentials.'
                    """)
    typewriter_print("\nWe defined username with user input and password with user input. Then we used an if statement to check if both the username and password are correct using the 'and' operator. This means both conditions must be true for the user to log in.\n")

    typewriter_print("Try it out yourself! Try putting User as the username and user123 as the password to see a successful login.\n")
    username = input("Enter username.. ")  
    password = input("Enter password.. ")

    while True:
        if (username == 'User') and (password == 'user123'):
            typewriter_print("\nUser Logged in")
            typewriter_print("(username == 'User') and (password == 'user123') is True internally.")
            break
        else:
            typewriter_print("\nWrong credentials, try again.\n")
            username = input("Enter username.. ")  
            password = input("Enter password.. ")

    typewriter_print("That is how conditional statements work using if and else!")
    wait_for_space()

def elif_match():
    os.system('cls')
    typewriter_print("Let's learn about conditional statements with elif now. For example, let's create a simple temperature level evaluator.")
    typewriter_print("""\nWe will use this code block:
temp = eval(input("Enter a number: "))

if temp == 0:
    print("Temperature is at the freezing point.")
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
                     
    This code checks the temperature input and categorizes it into different levels using if, elif, and else statements. When the user inputs a temperature, the program evaluates it against multiple conditions and prints the corresponding temperature level.""")

    typewriter_print("\nTry it out yourself!")
    while True:
        temp = input("\nEnter a number or type 'exit' to quit: ")
        temp = eval(temp) if temp.lower() != 'exit' else 'exit'

        if temp == 'exit':
            break
        elif temp == 0:
            typewriter_print("Temperature is at the freezing point.\n")
        elif temp >=1 and temp <= 20:
            typewriter_print("Temperature is very cold.\n")
        elif temp >=21 and temp <= 30:
            typewriter_print("Temperature is cold.\n")
        elif temp >=31 and temp <= 37:
            typewriter_print("Temperature is normal.\n")
        elif temp >=38 and temp <= 45:
            typewriter_print("Temperature is hot.\n")
        elif temp >=46 and temp <= 60:
            typewriter_print("Temperature is boiling hot.\n")
        elif temp > 60:
            typewriter_print("Temperature is at the burning point.\n")
        else:
            typewriter_print("Invalid input.\n")
    wait_for_space()

def for_loop():
    os.system('cls')
    typewriter_print("Let's learn about for loops in Python. For loops are used to iterate over a sequence (like a list, or string) or other iterable objects.")
    typewriter_print("""\nFor example, let's use a for loop to print each character in a string:
                     
for loop in range(1,100,1):
print(loop, "- Hello World")
                    
How many times do you think 'Hello World' will be printed..........?
                     
Times up! 
                     
It will be printed 99 times! The range(1,100,1) function generates numbers from 1 to 99 (100 is excluded), and the loop iterates over each number, printing 'Hello World' each time.""")
    
    typewriter_print("\nTry it out yourself!")
    while True:
        user_input = input("\nType a number to see how many times 'Hello World' will be printed (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        elif not user_input.isdigit():
            typewriter_print("Please enter a valid positive integer.")
        else:
            count = int(user_input)
            typewriter_print(f"\nPrinting 'Hello World' {count} times:\n")
            for loop in range(count):
                typewriter_print(f"{loop + 1} - Hello World")
    
    typewriter_print("""\nThe code we used for this function is:
                     
user_input = input("\\nType a number to see how many times 'Hello World' will be printed (or type 'exit' to quit): ")
                     
if user_input.lower() == 'exit':
    break
elif not user_input.isdigit():
    typewriter_print("Please enter a valid positive integer.")
else:
    count = int(user_input)
    typewriter_print(f"\\nPrinting 'Hello World' {count} times:\\n")
    for loop in range(count):
        typewriter_print(f"{loop + 1} - Hello World")
                     
This code prompts the user for a number and uses a for loop to print 'Hello World' that many times.""")
    
    typewriter_print("We can also use for loop to do incrementation and decrementation of values.")
    typewriter_print("""\nFor example, let's increment the value of a variable using a for loop:
                     
value = 0

for loop in range(1,5,1):
    print(loop)
    number = int(input("Enter a number: "))
    value += number

print("The total is", value)
                     
In this code, we initialize a variable 'value' to 0. The for loop runs 4 times (from 1 to 4). In each iteration, it prompts the user to enter a number and adds that number to 'value' using the '+=' operator. Finally, it prints the total value after the loop completes.""")
    
    typewriter_print("\nTry it out yourself!")

    while True: # Input validation loop with safety check
        value = input("\nInput a value to be added value to four times or 'exit' to quit: ")
        if value.lower() == 'exit':
            break
        elif not value.isdigit():
            typewriter_print("Please enter a valid number.")
        else:
            value = int(value)       
            for loop in range(1,5,1):
                typewriter_print(f"\nIteration {loop}:")
                number = eval(input("Enter a number: "))
                value += number

            typewriter_print(f"\nThe total is {value}")
            break

    typewriter_print("""\nThe code we used for this function is:
                     
value = input("\\nInput a value to be added value to four times: ")
                     
if value.isnotdigit():
    typewriter_print("Please enter a valid number.")
else:
    value = int(value)       
    for loop in range(1,5,1):
        typewriter_print(f"\\nIteration {loop}:")
        number = eval(input("Enter a number: "))
        value += number

        typewriter_print(f"\\nThe total is {value}")
                     
This code prompts the user for an initial value and then uses a for loop to increment that value by user-inputted numbers over 4 iterations.""")

    typewriter_print("""We can also use for loop to create patterns. For example with this code block:

for i in range(1,10,1):
    for x in range(10, i, -1):
        print(" ", end="")
    for y in range(1, i, 1):
        print("*", end="")
    for z in range(i, 1, -1):
        print("*", end="")
print()
                     
    This code creates a pyramid pattern using asterisks (*). The outer loop iterates from 1 to 9, controlling the number of rows. The first inner loop prints spaces to center the pyramid, the second inner loop prints increasing asterisks, and the third inner loop prints decreasing asterisks to complete each row of the pyramid.""")

    typewriter_print("\nLet's run the code.")

    for i in range(1,10,1):
        for x in range(10, i, -1):
            typewriter_print(" ", end="")
        for y in range(1, i, 1):
            typewriter_print("*", end="")
        for z in range(i, 1, -1):
            typewriter_print("*", end="")
        typewriter_print("")  # newline

    typewriter_print("\nThere is also a lot more shapes and patterns you can create using for loops. Explore and have fun with it! That's how you can use loops in python.")
    wait_for_space()

def random_module():
    os.system('cls')
    typewriter_print("""Let's learn about the random module in Python. The random module provides functions that generate random numbers and make random selections.
                     
Let's use this code block:
                     
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
                     
This code implements a simple number guessing game. It generates a random number between 1 and 10, and the user has 3 attempts to guess it. After each guess, the program provides feedback on whether the guess was too low, too high, or correct.""")
    
    typewriter_print("\nTry it out yourself!")
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
    
    typewriter_print("\nThe random module is a powerful tool for generating random numbers and making random selections in Python. Explore its various functions to enhance your programs with randomness!")
    wait_for_space()

def dictionaries():
    os.system('cls')
    typewriter_print("Let's learn about dictionaries in Python. A dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value.")

    typewriter_print("""\nFor example, let's create a simple dictionary to store information about months:
                     
months = ['Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun' , 'Jul']

for month in months:
  print(f"Month of {month}")
  
months.reverse()
print(months)
                     
This code creates a list of months and then iterates over the list to print each month. It also demonstrates how to reverse the list using the reverse() method.""")
    
    typewriter_print("The code will print the following:\n")

    months = ['Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun' , 'Jul']
    for month in months:
        typewriter_print(f"Month of {month}")
    months.reverse()
    typewriter_print(str(months))

    typewriter_print("\nThere's a lot of various uses of dictionaries in Python. For example, let's try making a simple student record system using dictionaries.")
    typewriter_print("""\nWe will use this code block:
                     
students = {
    '001': {'name': 'Alice', 'age': 20, 'major': 'Computer Science'},
    '002': {'name': 'Bob', 'age': 22, 'major': 'Mathematics'},
    '003': {'name': 'Charlie', 'age': 21, 'major': 'Physics'}
}
                     
for student_id, info in students.items():
    print(f"Student ID: {student_id}")
    for key, value in info.items():
        print(f"  {key.capitalize()}: {value}")
                     
                     
Here, we create a dictionary called 'students' where each key is a student ID and the value is another dictionary containing the student's name, age, and major. We then use nested for loops to iterate over the dictionary and print each student's information. Printing:""")
    
    students = {
        '001': {'name': 'Alice', 'age': 20, 'major': 'Computer Science'},
        '002': {'name': 'Bob', 'age': 22, 'major': 'Mathematics'},
        '003': {'name': 'Charlie', 'age': 21, 'major': 'Physics'}
    }
    for student_id, info in students.items():
        typewriter_print(f"\nStudent ID: {student_id}")
        for key, value in info.items():
            typewriter_print(f"  {key.capitalize()}: {value}")

    typewriter_print("\nDictionaries are versatile and can be used in various applications, such as storing configurations, managing data records, and more.")

    typewriter_print("To store data in a dictionary, you can define key-value pairs using curly braces {}. You can access values by their keys, add new key-value pairs, and modify existing ones using the assignment operator (=).")

    typewriter_print("""\nFor example: 
                     
student = {}
student['name'] = 'David'
student['age'] = 23
student['major'] = 'Biology'
print(student)

This code creates an empty dictionary called 'student' and then adds key-value pairs for the student's name, age, and major. Finally, it prints the dictionary to show the stored data. But what if we have multiple students to store, like how would we store data on two different students? We can use a list to store multiple dictionaries, each representing a student.Like:
                     
students = []
student1 = {'name': 'Eve', 'age': 24, 'major': 'Chemistry'}
student2 = {'name': 'Frank', 'age': 25, 'major': 'History'}
students.append(student1)
students.append(student2)
                     
print(students)
                        
This code creates an empty list called 'students' and then defines two dictionaries, 'student1' and 'student2', each representing a different student. It appends both dictionaries to the 'students' list and then prints the list to show the stored data for multiple students.""")
    wait_for_space()

def write_code():
    os.system('cls')
    typewriter_print("You can write your own code here to test and experiment with Python concepts you've learned!")
    typewriter_print("Type out a codeblock below (type 'end' on a new line and press enter to run the code):\n")
    typewriter_print("This is a dynamic code execution environment.When you press enter, you cannot delete the previous line, type reset to restart.\n")

    code_lines = []
    while True:
        line = input()
        if line.strip().lower() == 'end':
            break
        if line.strip().lower() == 'reset':
            code_lines = []
            os.system('cls')
            typewriter_print("Code reset. Start typing your code again (type 'end' on a new line to run):\n")
            continue
        code_lines.append(line)
    code_block = "\n".join(code_lines)
    typewriter_print("\nExecuting your code...\n")

    try:
        print()
        exec(code_block)
    except Exception as e:
        typewriter_print(f"An error occurred: {e}")
    wait_for_space()

def ending_message():
    os.system('cls')
    typewriter_print("Congratulations! You've completed the Interactive Python Program.")
    typewriter_print("We hope you enjoyed learning about Python programming concepts through this interactive experience.")
    typewriter_print("Keep practicing and exploring more about Python to enhance your skills further.")
    typewriter_print("Thank you for using this program!")