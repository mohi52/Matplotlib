import matplotlib.pyplot as plt

color = ["red", "green", "pink", "black", "gold"]
lb = ["Toyota", "Ford", "BMW", "Mercedes", "Honda"]
val = [38, 26, 29, 53, 76]

plt.pie(val, labels=lb, colors=color, shadow=True, radius=1.2)
plt.title('Диаграмма')
plt.show()