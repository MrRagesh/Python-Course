"""
step 1 : import necessary libraries
"""

import pandas as pd

mtcars_data = pd.read_csv(filepath_or_buffer="mtcars.csv")
print(mtcars_data)