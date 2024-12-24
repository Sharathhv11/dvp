import seaborn as sns
from pandas import read_csv
import matplotlib.pyplot as plt


"""
USN,Name,20CH201,20MA202,20EC203,20ME204,20CS205,20CH206
4MC24CS416,Sharath,80,70,90,78,67,89
4MC24CS417,xyz,80,70,90,78,67,89

"""

df = read_csv("./data.csv")

df.head()

student_data = df[["USN","20CH201","20MA202","20EC203","20ME204","20CS205","20CH206"]].set_index("USN")

std1 = student_data.loc["4MC24CS416"]
std2 = student_data.loc["4MC24CS417"]

fig,axes = plt.subplots(1,2,figsize=(7,7))

sns.barplot(ax=axes[0],x=std1.index,y=std1.values)

sns.lineplot(ax=axes[1],x=std2.index,y=std2.values)

fig.show()
