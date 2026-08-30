# Matplotlib for Data Analytics.
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # Generate 1000 random numbers from a normal distribution

plt.boxplot(data)
plt.title("Simple Box Plot")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.show()