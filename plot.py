import matplotlib.pyplot as plt
from random import randint

length = 10 # длина графика по оси х
y = [randint(10, 50) for i in range(length)]
x = [i for i in range(length)]

width = randint(2, 10) # ширина линии и маркера
color = ["red", "orange", "yellow", "green", "blue", 
         "purple", "pink", "brown", "black", "gray", 
         "silver", "gold", "beige", "turquoise", "cyan", 
         "magenta", "lime", "maroon", "navy", "olive", 
         "teal", "violet", "indigo", "coral"]

plt.plot(x, y, c=color[randint(0, len(color)-1)], lw=width, marker='o', ls='-', ms=width+5)
plt.title('Случайный линейный график') #заголовок
plt.grid()
plt.show()