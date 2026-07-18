"""
chapter 5 - How to deal with missing data

Handling Missing Bata

if case any missing data from the client file this steps to implement

1. I will call to my client, and check with him if he can give the right data
2. Incase, client is asking us to perform the data cleaning operations.

"""
import pandas as pd

emp_detailes = pd.read_csv(filepath_or_buffer="employee_data.csv")
print(emp_detailes)
print("")

# step 1 : remove duplicate entires/records
print("Removed duplicate entires : ")
emp_detailes.drop_duplicates(inplace=True) # inplace - the complete operations will impact the original dataset
print(emp_detailes)
print("")

print("Shape of employee data : ")
print(emp_detailes.shape)
print("")

# step 2 : find out the Null entries
print("find out the Null entries :")
find_null = emp_detailes.isnull().sum()
print(find_null)
print("")

# remove the null values using the function is ( .dropna() )
remove_missing_values = emp_detailes.dropna()
print(remove_missing_values)
print("")


print("Shape of employee data : ")
print(remove_missing_values.shape)
print("")

# step 3 : record in a document
"""
- client gave totally 7 observations out of which 3 entries are removed because those
  records do not have complete information.
"""

# step 4 : get approval
""""
- send this to client and get the approval to proceed for model building on model training
"""

print("Check any null values : ")
print(remove_missing_values.isnull().sum())