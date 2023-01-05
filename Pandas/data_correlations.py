import pandas as pd
import matplotlib.pyplot as plt
# plt.style.use("dark_background")

data = pd.read_csv("correlation_data.csv")
x = data["Duration"]
y1 = data["Calories"]
y2 = data["Maxpulse"]
# print(f"\n{data.corr()}")

# plt.subplot(1,2,1)
# plt.scatter(x,y1)
# plt.xlabel("Duration")
# plt.ylabel("Calories")
# plt.grid(color="grey")

# plt.subplot(1,2,2)
# plt.scatter(x,y2)
# plt.xlabel("Duration")
# plt.ylabel("Max Pulse")
# plt.grid(color="grey")


# plt.show()

y = data["Duration"]

plt.hist(y)

plt.show()

