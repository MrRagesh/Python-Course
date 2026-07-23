
# step 1 : import necessary libraries

import pandas as pd
from pandas.core.methods import describe
from matplotlib import pyplot as plt

# step 2 : import dataset
"""
About Mtcars Data:
==================
The data was extracted form the 1974 motor trend us magazine, and consumption and 
10 aspects of automobile design and performance for 32 automobiles (1973 - 474 models).

Format 
mpg - miles(us) gallon
cyl - number of cylinders
disp - displacement (cu.in.)
hp - gross horsepower
drat - rear axle ratio
wt - weight (1000 lbs)
vs - engine (0 = V-shaped, 1 = straight)
am - transmission (0 = automatic, 1 = manual)
gear - number of forward gears
"""
mtcars_data = pd.read_csv(filepath_or_buffer="mtcars.csv")
print(mtcars_data, "\n")

# step 3 : data understanding

# 3.1 perform initial analysis
check_shape = mtcars_data.shape
print("To Check the Shape of the dataset : \n",check_shape, "\n")

check_null = mtcars_data.isna().sum() # also use the isna()
print("Check null values : \n", check_null, "\n")

_describe = mtcars_data.describe()
print("Describe : \n",_describe, "\n")

# 3.2 Perform data visualization for better understanding
# or import matplotlib.pyplot as plt



plt.hist(mtcars_data["mpg"]) # speaks about the distribution of one continuous data
plt.title("MPG Distribution")
plt.xlabel("MPG")
plt.ylabel("Frequency")
plt.show()

# Insights :
# {Your Task} upload the data and graph to the ChatGPT to get the INSIGHTS:


"""
2 types of datatypes

MUST KNOW :-
- what type data to use what type of chart we can use to study it.

1. discrete data - countable / can't be measured / can't be segregated
2. continuous data - it has some units / it can be measured / can be segregated (

- using histogram to use only one column data's can apply . don't give the 
wrong data  
"""