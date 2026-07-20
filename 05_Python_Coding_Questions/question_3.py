"""
3. write a program that handles division by zero using try-except
"""

num = int(input("Enter a numerator : "))
den = int(input("Enter a denominator : "))

try:
    result = num / den
    print(result)
except ZeroDivisionError:
    print("Zero Division Error!, Divide by zero")
except ValueError:
    print("Value Error!, Please enter a number")
finally:
    print("Program End !")