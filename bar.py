import matplotlib.pyplot as plt 
import random

len = 20 #количество столбов
x = []
y = []


for i in range(len):
    y.append(random.randint(10,50)) #длины столбов

for i in range(len):
    x.append(i+1)

plt.bar(x,y, color = "green",width = 0.9)
plt.title('Случайная столбчатая диаграмма')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.show()