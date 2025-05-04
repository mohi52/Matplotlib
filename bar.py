import matplotlib.pyplot as plt 
from random import randint

length = 20 # количество столбов
x = [i+1 for i in range(length)]
y = [randint(10, 50) for i in range(length)]

plt.bar(x, y, color="green", width=0.9)
plt.title("Случайная столбчатая диаграмма")
plt.xlabel("Категории")
plt.ylabel("Значения")
plt.show()