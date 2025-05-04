import matplotlib.pyplot as plt 

x = list(range(10)) 
ybar = [23, 34, 45, 56, 67, 78, 89, 76, 40, 45]
yplot = [12, 20, 33, 47, 34, 76, 54, 63, 24, 12]

plt.bar(x, ybar, color="gray", width=0.9, label="столбы")
plt.plot(x, yplot, c="red", lw=2, marker="o", ls="-.", label="линия")
plt.title("Комбинировнный график")
plt.legend()
plt.grid()
plt.show()