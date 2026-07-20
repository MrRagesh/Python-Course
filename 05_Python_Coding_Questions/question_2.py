"""
2. create a list of numbers and print only even numbers using a for loop.
"""

numbers = range(1,51)
emp_list = []

for i in numbers:
    if i % 2 == 0:
        emp_list.append(i)
        
print(emp_list)
