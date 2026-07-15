"""
pandas library for data analysis

pip install pandas
pip - preferred installer program
use "r" read from the another directory r"C:\\user\ragesh\\.......
"""

import pandas as pd     # pd - means to refer Alias (nick name).

insurance_charges = pd.read_csv(filepath_or_buffer = r"insurance.csv")
print(insurance_charges)