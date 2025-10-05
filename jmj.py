import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
grades = np.random.randint(50, 101, 100)

plt.figure(figsize=(10, 6))
plt.hist(grades, bins=10, color='skyblue', edgecolor='black')
plt.title('Распределение оценок студентов')
plt.xlabel('Оценки')
plt.ylabel('Количество студентов')
plt.show()