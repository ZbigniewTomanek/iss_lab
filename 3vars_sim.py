from matplotlib import pyplot as plt
import numpy as np


def make_sim(x0, y0, z0, T, h, a0=1, a1=1, a2=1):
    t = [(T * (i/T)) for i in range(int(T/h))]
    x = [x0] * len(t)
    y = [y0] * len(t)
    z = [z0] * len(t)

    for i in range(1, len(t)):
        x[i] = x[i-1] + h * y[i-1]
        y[i] = y[i-1] + h * h * z[i-1]
        z[i] = z[i-1] + h * (-a0 * x[i] - a1 * y[i] - a2 * z[i])

    t = np.array(t)
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)

    return t*h, x, y, z


def plot_sims(N=1, T=10, h=0.01):
    x0 = 1
    y0 = 0
    z0 = 1
    fig, ax = plt.subplots()
    ax.set_xlabel('Stan')
    ax.set_ylabel('Wartość')

    gauss = np.random.normal(size=N)

    for i in range(N):
        t, x, y, z = make_sim(x0, y0, z0, T, h)
        ax.plot(t, x, label='x')
        ax.plot(t, y, label='y')
        ax.plot(t, z, label='z')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    plot_sims()
