# Seaborn for Data Analytics.
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
print(df.head())        # print top 5 rows.

sns.lineplot(x='size', y='tip', data=df, hue='sex')
plt.title("Line Plot - Tips Dataset") 
# plt.savefig("38S_LinePlot.png", bbox_inches="tight") # relative path
plt.show() 
