# Seaborn for Data Analytics.
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
print(df.head())        # print top 5 rows.

sns.barplot(x='size', y='tip', data=df, hue='sex')
plt.title("Bar Plot - Tips Dataset") 
# plt.savefig("39S_BarPlot.png", bbox_inches="tight") # relative path
plt.show()  


# Bar Plot show Mean & Variance of the data. It is used to show the relationship between a numerical and a categorical variable.