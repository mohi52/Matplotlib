import matplotlib.pyplot as plt
from random import randint

len = 50 # длина графика по оси х
x = [randint(-10, 10) for i in range(len)]

plt.hist(x, edgecolor='white', hatch='-')
plt.title('Гистограмма')
plt.show()