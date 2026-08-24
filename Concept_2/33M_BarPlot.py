# Matplotlib for Data Analytics.
import matplotlib.pyplot as plt
import numpy as np

x = ["A", "B", "C"]     # datatype is list
y = [10, 20, 15]        # datatype is list

plt.bar(x, y, color='blue', width=0.5, alpha=0.7, edgecolor='black')
plt.title("Simple Bar Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show() 


#Q. In this program, why we uaed numpy library?
#A. In this specific code snippet, the `numpy` library is imported but not actually used. The import statement for `numpy` is unnecessary in this case, as the code only utilizes lists for the x and y values in the bar plot. The `numpy` library is typically used for numerical operations and array manipulations, but since the code does not perform any such operations, it can be removed without affecting the functionality of the bar plot.