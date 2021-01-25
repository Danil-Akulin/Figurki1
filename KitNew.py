import numpy as np
import numpy
import matplotlib.pyplot as plt

fail = open(r'C:\ldpr\text_num.txt', 'r')
mas1 = []
mas2 = []
for line in fail:
    n = line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()
#print(mas1)
#print(mas2)

fig, ax = plt.subplots()

data = [mas2]

bins_to_be = 11
n, bins, patches = ax.hist(data, bins=bins_to_be,
                               color="brown", edgecolor="black")

res = ""
for i in range(bins_to_be):
    res += format(mas1)

ax.legend([res.strip()])
plt.show()




plt.subplots()
plt.title("y = abs(x**2 + 4*x - 5)")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")
plt.grid(axis="x", color="green", alpha=.3, linewidth=5, linestyle=":")
plt.grid(True)

x1 = np.arange(0, 10)
y1 = (2/27) * x1**2 - 3

x2 = np.arange(-10, 1)
y2 = 0.04 * x2**2 - 3

x3 = np.arange(-9, -3)
y3 = (2/9) * ((x3+6)**2)+1

x4 = np.arange(-4, 10)
y4 = -1*(1/12)*((x4-3)**2)+6

x5 = np.arange(5, 8.3)
y5 = (1/9)*((x5-5)**2) +2

x6 = np.arange(5, 8.5)
y6 = (1/8)*((x6-7)**2)+1.5

x7 = np.arange(-13, -8)
y7 = -1*0.75*((x7+11)**2)+6

x8 = np.arange(-15, -12)
y8 = -1*0.5*((x8+13)**2)+3

x9 = np.arange(-15, -9)
y9 = [1] * len(x9)

x10 = np.arange(3, 5)
y10 = [3] * len(x10)

plt.savefig('my.image.png')
plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10, '--r', label='парабола')
plt.show()

plt.subplots()
plt.title("Очки")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")
plt.grid(axis="x", color="red", alpha=.3, linewidth=6, linestyle=':')
plt.xticks(np.arange(-10, 10, 2))
plt.grid(True)

x1 = np.arange(-9, 0)
y1 = -(1/16)*((x1+5)**2)+2

x2 = np.arange(1, 10)
y2 = -(1/16)*((x2-5)**2) + 2

x3 = np.arange(-9, 0)
y3 = (1/4)*((x3+5)**2) - 3

x4 = np.arange(1, 10)
y4 = (1/4)*((x4-5)**2) - 3

x5 = np.arange(-9, -6)
y5 = (-(x5+7)**2) + 5

x6 = np.arange(6, 10)
y6 = (-(x6-7)**2) + 5

x7 = np.arange(-1, 2)
y7 = ((-0.5)*x7**2) + 1.5

plt.savefig('my.image.png')
plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7, '--r', label='парабола')
plt.show()

plt.subplots()
plt.title("Зонтик")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")
plt.grid(axis="x", color="blue", alpha=.3, linewidth=6, linestyle=':')
plt.xticks(np.arange(-15, 15, 5))
plt.grid(True)

x1 = np.arange(-12, 12)
y1 = (-(1/18)*x1**2) + 12

x2 = np.arange(-4, 5)
y2 = (-(1/8)*x2**2) + 6

x3 = np.arange(-12, -3)
y3 = -(1/8)*((x3+8)**2) + 6

x4 = np.arange(4, 12)
y4 = -(1/8)*((x4-8)**2) + 6

x5 = np.arange(-4, -0.5)
y5 = 2*((x5+3)**2) - 9

x6 = np.arange(-4, 1)
y6 = 1.5*((x6+3)**2) - 10

plt.savefig('my.image.png')
plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6, '--r', label='парабола')
plt.show()
