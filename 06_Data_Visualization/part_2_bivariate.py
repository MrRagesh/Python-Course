"""
3.2.2 Bivariate Analysis
"""

import matplotlib.pyplot as plt
import pandas as pd

mtcars_data = pd.read_csv(filepath_or_buffer="mtcars.csv")
print(mtcars_data.head(), "\n")

plt.bar(mtcars_data["hp"], height=mtcars_data["wt"])
plt.show()

# ============================================

import seaborn as sns

sns.barplot(data=mtcars_data, x="cyl", y="mpg") # importent! X - discrete and Y - continous thats why i using the seaborn - barplot
plt.title("mpg vs cyl")
plt.xlabel("cyl")
plt.ylabel("mpg")
plt.show()

"""
4 celiyenders cars in giving the average 27 milage per galan
6 cars giving 20 and 8 cars to giving 15

overall when the number of celynders geting increase the milage of the car getting decrease
"""