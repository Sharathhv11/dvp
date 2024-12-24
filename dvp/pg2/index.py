from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt

df  = read_csv("./data.csv")
sns.set_style("whitegrid")

sns.relplot(x="Maths Score",y="Science Score",hue="Gender",style="Parent Degree",data=df)

plt.show()