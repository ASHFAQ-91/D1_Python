# Seaborn for Data Analytics.
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
print(df.head())        # print top 5 rows.

sns.scatterplot(x='total_bill', y='tip', data=df, hue='sex')
plt.title("Scatter Plot - Tips Dataset") 
# plt.savefig("37S_ScatterPlot.png", bbox_inches="tight") # relative path
plt.show()