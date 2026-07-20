"""
6. create a dictionary with at least 5 key-value pairs and print them.
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
print(learners_detailes.to_csv(path_or_buf="learner_detailes.csv"))