"""
module 2.4.6
Number guessing game Level 6
Level 6. how to handle Invalid characters or values

exceptional handling
"""

import random

print("Welcome to Number Guessing Game!!")
print("Guess the Number between 1 - 100")

secret_number = random.randint(1,100)

for i in range(1,8):
    try:
        user_input = int(input("Enter the number: "))

        if user_input < 1 or user_input > 100:
            print("Invalid Number!!, Please enter the number between 1-100")
        elif user_input > secret_number:
            print("Sorry, the number you entered is too high!")
        elif user_input < secret_number:
            print("Sorry, the number you entered is too low!")
        else:
            print("your guessed number is correct!")
            break

    except ValueError:
        print("Invalid Characters, Please enter the number between 1-100 to play this game!")

if user_input == secret_number:
    print(f"Congradulations, You have the number {secret_number} in {i} attempts")
else:
    print("Sorry!, All your trials is exceeded!, Try Again!")