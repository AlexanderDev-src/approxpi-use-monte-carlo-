import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

n = 1000000

x = np.random.uniform(-1,1,n)
y = np.random.uniform(-1,1,n)


distance = np.sqrt(x**2 + y**2)

in_side = distance <= 1
out_side = ~in_side

pi = 4*np.sum(in_side)/n

print(f"PI = {pi}")
plt.figure(figsize=(7,7))
plt.plot(x[in_side],y[in_side],".",color='r')
plt.plot(x[out_side],y[out_side],".",color='b')
circle_plot = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
plt.gca().add_artist(circle_plot)

plt.show()
