"""
3.3.3 Multivariate Analysis

-> more then 2 features
that using pairplot

we using the pandas that only displaying in the table format we can't see the visualization
but we want to take quicke decision from the data we want to use the data visulizaition and thats why i using the data
visualization matplotlib, seaborn and plotly
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

mtcars_data = pd.read_csv(filepath_or_buffer="mtcars.csv")
print(mtcars_data.head(), "\n")

sns.barplot(data=mtcars_data, x="cyl", y="disp")
plt.title("Displacement vs cyl")
plt.xlabel("Displacement")
plt.ylabel("cyl")
plt.show()

sns.pairplot(data=mtcars_data)
plt.show()