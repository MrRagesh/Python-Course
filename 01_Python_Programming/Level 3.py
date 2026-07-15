print("Welcome to Number Guessing Game!!")
print("Guess the Number between 1 - 100")

secret_number = 98

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
        print(f"Congradulations, You have the number {secret_number} in {i} attempts")
        break
