"""
10. Filter rows in a DataFrame where the "Age" column in greater than 30.
"""

import pandas as pd

emp_data = pd.read_csv(filepath_or_buffer="employee_data.csv")
print(emp_data)
print("")

filter_age = emp_data["Age"] > 30
print(filter_age)
print("")
print(emp_data[filter_age])