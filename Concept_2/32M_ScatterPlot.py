# Matplotlib for Data Analytics.
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]             # datatype is list
y = [10, 20, 15, 30, 25]        # datatype is list

plt.scatter(x,y, c='red', s=100, alpha=0.5, marker='o', edgecolors='black')
plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


#Q. In this program, why we uaed numpy library?
#A. In this specific code snippet, the `numpy` library is imported but not actually used. The import statement for `numpy` is unnecessary in this case, as the code only utilizes lists for the x and y values in the scatter plot. The `numpy` library is typically used for numerical operations and array manipulations, but since the code does not perform any such operations, it can be removed without affecting the functionality of the scatter plot.