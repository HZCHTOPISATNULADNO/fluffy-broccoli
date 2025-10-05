import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import xlabel, ylabel

np.random.seed(0)
height = np.random.normal(170, 10, 50)
weight = np.random.normal(70, 15, 50)
plt.figure(figsize=(10, 6))
plt.scatter(height, weight, color='r')
xlabel('height')
ylabel('weight')
plt.show()