import pandas as pd

my_dataset = {
    "cars":  ["BMW","Volvo","Ford"],
    "passings": [3,7,2]
}

my_var = pd.DataFrame(my_dataset)
print(pd.__version__)
print(my_var)