"""
chapter 4. Filtering | Selection | Sorting or indexing

to learning the
indexing, selection, and filtering

pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None) (TO REMOVE THE LIMITATION'S OF ROWS AND COLUMNS)

"""

import pandas as pd

euro_data = pd.read_csv("Euro_2012_stats_TEAM.csv")
# filter we can to take team, goals, red card, yello card

pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
print(euro_data)
print("")

# Filtering
print("To Display the Importent columns ")
filtered_euro_data = euro_data[["Team","Goals","Red Cards", "Yellow Cards", ]] # more then one column we can use the python data structure (list, tuple, set , dict)
print(filtered_euro_data)
print("")

print("Top 5 Yellow Cards Team : ")
yellow_cards = filtered_euro_data.sort_values(by="Yellow Cards", ascending=False).head(5) #sorting the high to low
print(yellow_cards)
print("")

# Selection
# 4.2 list the teams which has got red card
print("list the teams which has got red card : ")
red_cards = filtered_euro_data[filtered_euro_data["Red Cards"] == 1]
print(red_cards)
print("")

# 4.3 list teams which has got more than 8 yellow cards
print("list teams which has got more than 8 yellow cards ")
yellow_8 = filtered_euro_data[filtered_euro_data["Yellow Cards"] >= 8]
print(yellow_8)
print("")

""""
Task
1. Find out 5 New questions along with script answers
"""

# filtered
print("We can how many passes in the ball above 1500 passes team list : ")
ball_passes = euro_data[["Team" , "Passes"]]
print(ball_passes)
print("")

#above 1500 passes
ball_passes = ball_passes[ball_passes["Passes"] >= 1500]
print(ball_passes)
print("")

"""
print(euro_data["Team", "Goals"]) -> it's causes KeyError: ('Team', 'Goals') error 
the default to output give in tuple so it's shows the error
"""