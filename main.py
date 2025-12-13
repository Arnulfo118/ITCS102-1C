from functions import *
import os

topics = [
    "1. Basic Print Statements",
    "2. Advanced Print Statements",
    "3. Input Handling",
    "4. Eval Function",
    "5. Equations",
    "6. Augmented Assignments",
    "7. String Concatenation",
    "8. If Statements",
    "9. If with Elif and Else",
    "10. For Loops",
    "11. Random Module",
    "12. Dictionaries",
    "13. Write Your Own Code",
]

completed_topics = set(range(1, 12))  # For testing purposes, all topics marked as completed

while True:
    os.system('cls')
    typewriter_print("Welcome to the Interactive Program!\n")
    typewriter_print("This program teaches you Python interactively. Let's get started!\n")
    typewriter_print("Please select a topic to learn about (1-12) or type 'exit' to quit and or type 'finished' if you have already done everything:") #typing 'finished' will show all topics as completed and do the ending message.

    for i, topic in enumerate(topics, start=1): # Display topics with completion status exception for "Write Your Own Code"
        if i in completed_topics and i != 13:
            typewriter_print(topic + "  ✔", delay=0)
        else:
            typewriter_print(topic, delay=0)
    
    choice = input("\nYour choice:  ")
    if choice.lower() == 'exit' or choice.lower() == 'x':
        os.system('cls')
        ending_message()
        break

    elif choice.lower() == 'finished':
        completed_topics = set(range(1, 13))
        os.system('cls')
        ending_message()
        break

    if choice.isdigit() and 1 <= int(choice) <= 13:
        choice = int(choice)
        if choice == 1:
            basic_print()
        elif choice == 2:
            advanced_print()
        elif choice == 3:
            input_function()
        elif choice == 4:
            eval_function()
        elif choice == 5:
            equationals()
        elif choice == 6:
            augmented_assignment()
        elif choice == 7:
            string_concatenation()
        elif choice == 8:
            if_match()
        elif choice == 9:
            elif_match()
        elif choice == 10:
            for_loop()
        elif choice == 11:
            random_module()
        elif choice == 12:
            dictionaries()
        elif choice == 13:
            write_code() # exception in completed topics tracking
        
                # Mark lesson as completed
        completed_topics.add(choice)

        # Check if ALL topics done
        if len(completed_topics) == 12:
            os.system('cls')
            ending_message()
            break
    else:
        typewriter_print("Invalid choice. Please select a number between 1 and 12 or type 'exit/x' to quit.\n")

