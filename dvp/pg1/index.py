import matplotlib.pyplot as plt
import csv

temp = []
date = []

with open("./data.csv") as file:
    data = csv.reader(file)

    for x in data:
        temp.append(x[1])
        date.append(x[0])


plt.plot(date,temp,linestyle="--",marker="o")

plt.title('temprature over time')
plt.xticks(rotation=45)
plt.xlabel("date")
plt.ylabel("temp")

plt.legend()

plt.show()

