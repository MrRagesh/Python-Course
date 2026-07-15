"""
3. matplotlib, seaborn, plotly - for data visualization

2 types of datatypes:
1. discrete - countable, it will never have any untils, you can't measure that
2. continous - it will have unites, it is measurable
"""
# or import matplotlib.pyplot as plt

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

insurance_charges = pd.read_csv(filepath_or_buffer="insurance.csv")

plt.hist(insurance_charges.age)
plt.show()

