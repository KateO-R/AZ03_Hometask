from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import csv
import re

driver = webdriver.Chrome()

url = "https://www.divan.ru/ekaterinburg/category/divany-i-kresla"

driver.get(url)
time.sleep(5)

prices = driver.find_elements(By.CSS_SELECTOR, "span.ui-LD-ZU")

with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
   writer = csv.writer(file)
   writer.writerow(['Price'])

   for price in prices:
       # Извлечение числовой части из текста
       price_text = price.text
       # Используем регулярное выражение для извлечения чисел
       price_number = re.sub(r'[^\d]', '', price_text)
       # Проверяем, что строка не пустая, и преобразуем в число
       if price_number:
           writer.writerow([int(price_number)])

driver.quit()

df = pd.read_csv('prices.csv')
average_price = df['Price'].mean().round(2)
print(f"Average sofa price from CSV - {average_price}")