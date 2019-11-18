import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from mpl_toolkits.mplot3d import Axes3D


def find_intersections(x, y):
    return np.argwhere(np.diff(np.sign(x - y))).flatten()

x0 = 1
y0 = -4

a = 0.5
b = 0.75

h = 0.01
T = 100

N = int(T/h)
t = np.linspace(0, T, N)
x = np.zeros((N,))
y = np.zeros((N,))
z = np.zeros((N,))
x[0] = x0
y[0] = y0

for i in range(1, N):
    print(x[i-1])
    xp = (np.power(x[i-1], 3)) / 3
    print(xp)
    x[i] = x[i-1] + h*(-y[i-1] + x[i-1] - xp + 0.4)
    y[i] = y[i-1] + h*(x[i-1] + a - b*y[i-1])


# peaks_x, _ = find_peaks(x)
# dips_x, _ = find_peaks(-x)
#
# peaks_z, _ = find_peaks(z)
# dips_z, _ = find_peaks(-z)

plt.figure(1)
plt.plot(t, x)
plt.plot(t, y)


plt.figure(2)
plt.plot(x, y)
# plt.plot(x[peaks_x], z[peaks_x], "bo")
# plt.plot(x[dips_x], z[dips_x], "ro")
# plt.plot(x[peaks_z], z[peaks_z], "bx")
# plt.plot(x[dips_z], z[dips_z], "rx")


# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()

plt.show()
