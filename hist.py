import matplotlib.pyplot as plt
import random

len = 50 #длина графика по оси х
x = []

for i in range(len):
    x.append(random.randint(-10,10))

plt.hist(x,edgecolor = 'white',hatch = '-')

plt.show()