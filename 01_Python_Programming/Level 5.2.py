"""
5.2 take out the limits for try

so to remove the for loop
implement the while loop for unlimited numbers entered
"""

import random

print("Welcome to Number Guessing Game!!")
print("Guess the Number between 1 - 100")

secret_number = random.randint(1,100)
i = 0

while True:

    user_input = int(input("Enter the number: "))

    if user_input < 1 or user_input > 100:
        print("Invalid Number!!, Please enter the number between 1-100")
    elif user_input > secret_number:
        print("Sorry, the number you entered is too high!")
        i = i + 1
    elif user_input < secret_number:
        print("Sorry, the number you entered is too low!")
        i = i + 1
    else:
        print("your guessed number is correct!")
        i = i + 1
        break

if user_input == secret_number:
    print(f"Congradulations, You have the number {secret_number} in {i} attempts")
else:
    print("Sorry!, All your trials is exceeded!, Try Again!")