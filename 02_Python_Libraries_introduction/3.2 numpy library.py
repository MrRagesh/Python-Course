"""
numpy -  for numerical operations
python also case sensitive
"""
import pandas as pd
import numpy as np

insurance_charges = pd.read_csv(filepath_or_buffer="insurance.csv")

filepath = np.repeat( a = insurance_charges, repeats=3, axis=0 )

insurance_data_updated = pd.DataFrame(data = filepath)

print(insurance_data_updated)