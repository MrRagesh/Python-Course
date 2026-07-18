
# 1.2 Find out the items sold in the restaurent

import pandas as pd

order_detailes = pd.read_csv(filepath_or_buffer="data.tsv.txt", sep="\t") #DataFrame
print(order_detailes)
print("")

unique_values = order_detailes.nunique()
print(unique_values)
print("")

single_item = order_detailes["item_name"].unique() # this function to get the dataframe to get the unique items or values
print(single_item)
print("")

# 1.3 Give me the list of Top 5 Selling Items

top_selling = order_detailes.groupby(by="item_name")["quantity"].sum().sort_values(ascending=False) # Chain of Functions or methods | very Importent (groupby()) function
print(top_selling)
print("")

# list the top 5 or 10 selling items

print("Top selling items:")
top_10 = top_selling.head(10)
print(top_10)
print("")

# list the least 5 selling items

print("Least 5 Selling Items: ")
top_5 = order_detailes.groupby(by="item_name")["quantity"].sum().sort_values().head(5)
print(top_5)
print("")
