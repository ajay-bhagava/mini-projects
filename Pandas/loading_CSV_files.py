import pandas as pd

# Loading Files into a Dataframe

exercise_csv_data = pd.read_csv("data.csv")
# print(exercise_csv_data)

# Use to_string() to print the entire thing instead of just first and last 5 rows
# print(exercise_csv_data.to_string())\

# change max rows with max_rows
# print(pd.options.display.max_rows) # checks the default max rows (60)

pd.options.display.max_rows = 9999
# print(exercise_csv_data)


# Wokring with JSON files
exersise_JSON_data = pd.read_json("data.json")

# print(exersise_JSON_data.to_string())

# JSONs have the same format as dictionaries
exercise_dictionary= {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

exercise_dictionary_data = pd.DataFrame(exercise_dictionary)

# print(exercise_dictionary_data)

















# View data: the head() and tail() defaults to the first/last 5 rows
# print(exercise_csv_data.head(10)) # reads the first 10 rows

# print(exercise_csv_data.tail(10)) # reads the last 10 rows


# print(exercise_csv_data.info()) # genearl info about dataset


