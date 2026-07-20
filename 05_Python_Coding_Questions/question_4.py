"""
4. given a string, count how many vowels it  has.
"""

user_input = input("Enter the senctence : ")
count = 0

for i in user_input:
    if i in "aeiou" or i in "AEIOU":
        print(i)
        count += 1

print(f"Total number of vowels : {count}")