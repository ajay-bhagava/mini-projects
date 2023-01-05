import pandas as pd

exercise_data = pd.read_csv("data_with_dates.csv")

# dropna() will not change the original dataframe
no_null_data = exercise_data.dropna()
# print(no_null_data.to_string())

# using inplace=true will change original dataframe

# no_null_data = exercise_data.dropna(inplace=True)
# print(exercise_data)



# fillna() fills nulls with a specified value
filled_data = exercise_data.fillna(130) # fills nulls regardless of column
filled_data_calories = exercise_data["Calories"].fillna(130) #specify column to fill
# print(filled_data.to_string()) 
# print(filled_data_calories.to_string()) 



# Remove data of wrong format
# exercise_data["Date"] = pd.to_datetime(exercise_data["Date"])
# This still leaves one row as NaT, which can be dropped with dropna
# exercise_data.dropna(subset=['Date'], inplace=True)
# print(exercise_data.to_string())










# Fixing wrong data
"""
# Replace wrong data
exercise_data.loc[7, "Duration"] = 45 # replaces row 7 in the duration column with 45

# for loop to change in bulk
for x in exercise_data.index:
    if exercise_data.loc([x, "Duration"]) > 120:
        exercise_data.loc([x, "Duration"]) = 120 # this just sets the value to 120
        # exercise_data.drop(x, inplace=True) # this would drop the whole row

"""

# print(exercise_data.duplicated()) # prints true if the row is a duplicate

exercise_data.drop_duplicates(inplace=True) # this drops duplicates
print(exercise_data)















