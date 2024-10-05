import matplotlib.pyplot as plt
import numpy as np

random_arrayX = np.random.rand(5)  # массив из 5 случайных чисел
random_arrayY = np.random.rand(5)

plt.scatter(random_arrayX, random_arrayY)

plt.xlabel("axis x")
plt.ylabel("axis y")
plt.title("Scatter diagram for 2 random data sets")

plt.show()

