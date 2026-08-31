# Matplotlib for Data Analytics.
import matplotlib.pyplot as plt
import numpy as np

winning = [48, 33, 19]  # datatype is list
heros = ['Batman', 'Ironman', 'Spiderman']  # datatype is list

plt.pie(winning, labels=heros, autopct='%d%%', startangle=90)
plt.title("Superhero Popularity - Pie Chart")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig("36M_PieChart.png", bbox_inches="tight") # relative path.
# plt.show()