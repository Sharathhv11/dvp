import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("./data.csv")

df.info()

# plt.figure(figsize=(20,8))

sns.set_style("whitegrid")

sns.violinplot(data=df,x="Education Level",y="Salary")
plt.show()

sns.boxenplot(data=df,x="Education Level",y="Salary")
plt.show()