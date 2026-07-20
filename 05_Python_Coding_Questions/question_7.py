"""
7. write a pandas code to read a CSV and print the top 5 rows.
"""

import pandas as pd


emp_detailes = pd.read_csv(filepath_or_buffer="employee_data.csv")

print(emp_detailes.head(5))

