"""
1. How to create our own module & import it like Pandas library?
2. Creating Modules VS Purpose of OOPS
3. How to create class, objects and inheritance methods and it's real-time purpose?
"""

# 1. How to create our own module & import it like Pandas library?

import pandas_math as pm

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

_add = pm.addition(a,b)

print("The addition function is called : ")
print(_add)

