"""
5. reverse a list without using built-in functions.
new_list = original_list[::-1]
"""

original_list =[1,2,3,4,5]
new_list = []
i = len(original_list) - 1

while i>=0:
    new_list.append(original_list[i])
    i = i - 1
print(new_list)

