"""
9. replace all missing values in a Dataframe with the column's mean.
"""
from statistics import mean

import pandas as pd

emp_data = pd.read_csv(filepath_or_buffer="employee_data.csv")
print(emp_data)
print("")

emp_data.fillna({"Salary" :  }, inplace=True)
print(emp_data)

"""emp_data["Salary"] = emp_data["Salary"].fillna(value = emp_data["Salary"].mean())
print(emp_data)
"""