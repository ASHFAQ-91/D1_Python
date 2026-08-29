# Matplotlib for Data Analytics.
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # Generate 1000 random numbers from a normal distribution

plt.hist(data, bins=9, color='green', alpha=0.7, edgecolor='black')
plt.title("Simple Histogram Plot")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.show()