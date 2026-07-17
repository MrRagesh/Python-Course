"""
chapter 3. pandas data structure

- 1d - series (either row or column)
- 2d - dataframe (both rows and columns)
"""

import pandas as pd

one_dimensional = pd.Series(data=[1,2,3,4]) # using the python data structure to implement
# using the list python data structure
print(one_dimensional)

# you can use the multidimensional data we use the {pd.DataFrame} function
two_dimensional = pd.DataFrame(data = {
    "names" : ["ragesh", "saru", "bala", "mohan","ram"],
    "maths" : [45,65,76,54,98],
    "science" : [100,65,99,89,98],
})

print(two_dimensional)