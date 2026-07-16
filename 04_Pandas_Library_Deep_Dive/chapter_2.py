"""
chapter 2: Data Cleaning

1. business understanding
2. data collection
3. data understanding
4. data preparation
"""

import pandas as pd

order_detailes = pd.read_csv(filepath_or_buffer="data.tsv.txt", sep="\t")
print(order_detailes)
print("")

data_types = order_detailes.dtypes # this is an attribute
print(data_types)
print("")

# Series
print("To remove the $ symbol in the item_price column :")
#to remove the Dollar $
remove_dollar = order_detailes["item_price"].str.replace("$", "").astype(float) # chain of methods
# .float() -> 'Series' object has no attribute 'float'. Did you mean: 'plot'?
"""
To convert a Pandas Series to float, use s = s.astype(float) for clean numeric data, 
or s = pd.to_numeric(s, errors='coerce') if your series contains unparseable strings 
or missing values.
"""
print(remove_dollar)
print("")

print("Old Order Detailes :")
print(order_detailes)
print("")

print("Updated Order Detailes :")
order_detailes["item_price"] = remove_dollar

print(order_detailes)

print(order_detailes.describe())

