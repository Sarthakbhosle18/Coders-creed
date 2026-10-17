import pandas as pd

arr = [10,20,30,40,50]
indexes= ["day1","day2","day3","day4","day5"]

data = {
    "day1":{"Calories":45,"Fat":56,"Protein":35,"Carbs":120},
    "day2":{"Calories":85,"Fat":59,"Protein":5,"Carbs":120},
    "day3":{"Calories":25,"Fat":54,"Protein":305,"Carbs":120},
    "day4":{"Calories":50,"Fat":96,"Protein":315,"Carbs":120},
    "day5":{"Calories":60,"Fat":56,"Protein":65,"Carbs":120},
    "day6":{"Calories":70,"Fat":76,"Protein":45,"Carbs":120},
    "day7":{"Calories":45,"Fat":51,"Protein":55,"Carbs":120},
    "day8":{"Calories":80,"Fat":30,"Protein":95,"Carbs":120},
    "day9":{"Calories":95,"Fat":80,"Protein":75,"Carbs":120},
    "day10":{"Calories":5,"Fat":42,"Protein":25,"Carbs":120},
}

# series

x = pd.Series(arr,index= indexes)
print("----Series value for day3----")
print(x["day3"]) 
print()

# Dataframe
y= pd.DataFrame(data)

# print the full dataframe to see how it looks
print("----Full DataFrame Layout----")
print(y)
print()

# Get a Specific Column (day2 data)
print("---data for day2---")
print(y["day2"])
print()

# Correct way to get a specific row using .loc with square brackets
print("----The entries fats row----")
print(y.loc["Fat"])

# get a specific single cell value (row:Fats,Column:day2)
print("----Fats value specifically for day2----")
print(y.loc["Fat","day2"])