"""
Task - Data Analytics

1. impute the relevant values in the salary column wherever it is NaN based on the
   department filtering.
2. impute mathiew's age as 27

"""

import pandas as pd
import  openpyxl

emp_detailes = pd.read_excel(io="employee_data.xlsx", sheet_name="more_employee")
print(emp_detailes)
print("")

# find the duplicate values
duplicate_data = emp_detailes.duplicated()
print(duplicate_data)
print("")

# delete the duplicate data
delete_duplicate = emp_detailes.drop_duplicates(inplace=True)
print(delete_duplicate)
print("")

# get all the department
departments = emp_detailes["Department"].unique()
print(departments)
print("")

# get the ops department
ops = emp_detailes[emp_detailes["Department"] == "Ops"]
print(ops)
print("")

ops_dep = emp_detailes[(emp_detailes["Department"] == "Ops") & (emp_detailes["Salary"].isna())]
print(ops_dep)
print("")

