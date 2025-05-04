import matplotlib.pyplot as plt
import random 


len = 10 #длина графика по оси х
y = []
x = []
for i in range(len):
    y.append(random.randint(10,50)) 

width = random.randint(2,10) #ширина линии и маркера
color = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "gray", "silver", "gold", "beige", "turquoise", "cyan", "magenta", "lime", "maroon", "navy", "olive", "teal", "violet", "indigo", "coral"]
 
for i in range(len):
   x.append(i)

plt.plot(x,y, c = color[random.randint(0,24)], lw = width, marker = 'o',ls = '-',ms = (width+5))
plt.title('Случайный линейный график') #заголовок
plt.grid()
plt.show()