import pandas as pd
import matplotlib.pyplot as plt

file_path = 'prices.csv'
data = pd.read_csv(file_path)

prices = data['Price']

# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Price histogram')
plt.xlabel('Price')
plt.ylabel('Frequency')

# Показать гистограмму
plt.show()