"""
Task

1. find out the top 5 selling items individual revenue it made.
2. total revenue of the top 5 items sold
"""

import pandas as pd

order_detailes = pd.read_csv(filepath_or_buffer="data.tsv.txt", sep="\t")
print(order_detailes)
print("")

print("To remove the dollar $ symbol :")
remove_dollar = order_detailes["item_price"].str.replace("$", "").astype(float)
print(remove_dollar)
print("")

order_detailes["item_price"] = remove_dollar

print("Top 5 selling items individual revenue :")
top_selling = order_detailes.groupby(by="item_name")["item_price"].sum().sort_values(ascending=False).head(5)
print(top_selling)
print("")

print("Total revenue of the top 5 selling items :")
total_revenue = top_selling.sum()
print(total_revenue)