"""
Chapter 1: getting & knowing your data

- meaning full insites -> the information don't know the client to find out the data analysis to tell them. so
he can take decision easy.
"""

import pandas as pd


order_detailes= pd.read_csv(filepath_or_buffer='data.tsv.txt', sep='\t')
print(order_detailes)
print("")

# 1.1 Perform Initial Analysis
#Function - ()
#Attribute - no gives value (shape) is a attribute

shape_data = order_detailes.shape
print(shape_data)

# Terminology Alert
    # Rows - Obsservation/Record
    # Column - Features/Parameters

null_entery = order_detailes.isnull().sum() # Chain of functions, chain of commands
print(null_entery)
print("")

data_types = order_detailes.dtypes
print(data_types)
print("")

statistic = order_detailes.describe(include="all")
print(statistic)
print("")

"""demo = pd.read_table(filepath_or_buffer="/Users/ragesh/Documents/Entire Projects/Python Course/02_Python_Libraries_introduction/insurance.csv", sep=",")
print(demo)

d1 = pd.read_table(filepath_or_buffer="data.tsv.txt")
print(d1)

"""


