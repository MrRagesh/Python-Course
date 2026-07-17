"""
task 2

1. create a meaningful series
2. create a meaningful dataset using pandas dataframe with dict 5 observation across 6 features
"""

import pandas as pd

fruites = ["apple", "banana", "orange", "mango", "grapes", "pineapple"]

print("One Dimensional Dataset :")
_series = pd.Series(data = fruites)
print(_series)
print("")

student_detailes = {
    "Name" : ["Ragesh", "Sarubala", "Mohan", "Mani", "Kumari"],
    "Roll No" : ["01", "02", "03", "04", "05"],
    "Age" : [20, 19, 20, 18, 21],
    "Sex" : ["Male", "Female", "Male", "Male", "Female"],
    "Department" : ["IT", "IT", "CSE", "EEE", "AI&DS"],
    "Grade" : ["A+", "O", "A", "B", "B+"],
}

print("Multidimensional Dataset :")
_dataframe = pd.DataFrame(data = student_detailes)
print(_dataframe)
print("")