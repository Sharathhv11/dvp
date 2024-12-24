from pandas import read_csv
import seaborn as sns
from matplotlib import pyplot as plt

data = read_csv("./data.csv")

sns.lineplot(data=data,x="Date",y="Open",hue="Symbol")


plt.show()