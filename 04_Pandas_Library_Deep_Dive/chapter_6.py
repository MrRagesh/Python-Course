"""
chapter 6 : Data Cleaning Techniques
level 2 - Data Cleaning Techniques
second part (Advanced Data Cleaning) methods

we can use the excel sheets mainly to install the
!pip install openpyxl -> open | python | excel
"""

import pandas as pd
import openpyxl
from numpy.ma.core import empty_like

""""
pd.read_csv() -> you can import multiple sheets if it's in the csv file
"""
emp_detailes = pd.read_excel(io="employee_data.xlsx", sheet_name="more_employee")
print(emp_detailes)
print("")

print("Before the shape of the dataframe : ")
before_shape = emp_detailes.shape
print(before_shape)
print("")

# step 1 : remove the duplicate entries
print("Remove the duplicate entries")
emp_detailes = emp_detailes.drop_duplicates()
print(emp_detailes)
print("")

print("After the shape of the dataframe : ")
after_shape = emp_detailes.shape
print(after_shape)
print("")

# step 2 : to find the null values
print("To find the Null values : ")
find_null = emp_detailes.isnull().sum()
print(find_null)
print("")

# step 3 : Delete the null entries
print("delete the null values :")
emp_detailes.dropna(inplace=True)
print(emp_detailes)
print(emp_detailes.shape)
print(emp_detailes.describe())



