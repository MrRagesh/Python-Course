"""
Chapter 1: getting & knowing your data
"""

import pandas as pd

demo = pd.read_csv(filepath_or_buffer='data.tsv.txt', sep='\t')

print(demo)
