import numpy as np
from matplotlib import pyplot as plt


def make_sim(x0=1, y0=-1,T=40, h=0.01, mi=2, w=0.7):
    t = [(T * (i/T)) for i in range(int(T/h))]
    x = [x0] * len(t)
    y = [y0] * len(t)

    for i in range(1, len(t)):
        x[i] = x[i-1] + h * y[i - 1]
        y[i] = y[i-1] + h * (-(w*w*x[i]) + mi * (1 - x[i] * x[i])*y[i-1])

    t = np.array(t)
    x = np.array(x)
    y = np.array(y)

    return t*h, x, y


def plot_sim():

    fig, ax = plt.subplots()
    ax.set_xlabel('Stan')
    ax.set_ylabel('Wartość')
    t, x, y = make_sim()
    ax.plot(t, x, label='x')
    ax.plot(t, y, label='y')

    plt.legend()
    plt.show()


if __name__ == '__main__':
   plot_sim()

