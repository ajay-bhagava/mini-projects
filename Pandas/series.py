import pandas as pd

a = [1,7,2]

var = pd.Series(a, index = ["x","y","z"])

# print(var)
# use index to access sngle value
# print(var["y"])


# series of a dictionary
calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}

# specifying only the indices day1 and day2 are included
caloriesSeries = pd.Series(calories, index=["day1","day2"])
# print(caloriesSeries)


# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

exerciseData = {
    "calories": [420,380,390],
    "duration": [30,40,45]
}

exercise_data_frame = pd.DataFrame(exerciseData, index = ["day1","day2","day3"])
# print(exercise_data_frame)

# locate a row in the data
# print(exercise_data_frame.loc[0])

# locate multiple rows with a list of indices
# print(exercise_data_frame.loc[[0,1]])

# locate a named index
# print(exercise_data_frame.loc["day2"])







