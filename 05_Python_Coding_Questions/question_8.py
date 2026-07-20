"""
8. create a Dataframe from a python dictionary
"""
import pandas as pd

learners_detailes = pd.DataFrame(data={
    "First Name ":["Moorhty", "Ragesh", "Charu"],
    "Last Name ": ["Kumar", "Kannan", "Bala"],
    "Age ": [20,21,19],
    "Location ": ["Chennai", "Trichy", "Palakurichy"],
    "Degree ": ["ECE", "IT", "CSE"]
})

print(learners_detailes)