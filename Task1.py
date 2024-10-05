import matplotlib.pyplot as plt
import numpy as np

mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов
data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=6)
plt.xlabel("axis x")
plt.ylabel("axis y")
plt.title("Histogram for random data")

plt.show()
