"""
module 2.4.4
number guessing game level 4
level 4. setting multiple conditions
"""

print("Welcome to Number Guessing Game!!")
print("Guess the Number between 1 - 100")

secret_number = 50

for i in range(1,8):
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

if user_input == secret_number:
    print(f"Congradulations, You have the number {secret_number} in {i} attempts")
else:
    print("Sorry!, All your trials is exceeded!, Try Again!")