import numpy as np
from matplotlib import pyplot as plt

# parametry symulacji
p_up = 2  # górny próg histerezt
p_down = -2  # dolny próg histerezy
ascending = False  # zmienna mówiąca o tym, czy wykres idzie do gory, czy w dol
x_req = 60  # wartość oczekiwana
x0 = 50  # wartość początkowa
T = 100  # czas trwania symulacji
a = -0.1  # współczynnik stygnięcia
u = 6.5  # wartość sterowania
h = 0.01  # wartość kroku


def steer(x):
    global ascending
    e = x_req - x
    print(x)
    if e > p_up:
        ascending = False
        return u
    elif e < p_down:
        ascending = True
        return 0
    elif p_down < e < p_up:
        if ascending:
            return 0
        else:
            return u


def make_simulation():
    N = int(T / h)
    t = np.linspace(0, T, N)
    all_x = np.zeros((N,))

    all_x[0] = x0
    steering = np.zeros((N,))
    error = np.zeros((N,))
    error[0] = x_req - x0

    for i in range(1, N):
        u_val = steer(all_x[i - 1])
        steering[i - 1] = u_val
        all_x[i] = all_x[i - 1] + h * (a * all_x[i - 1] + u_val)
        error[i] = x_req - all_x[i]

    plt.figure('Stan - sterowanie')
    ax = plt.subplot(311)
    ax.axhline(y=x_req, color='k')
    ax.set_title('Stan x')
    ax.plot(t, all_x)

    ax = plt.subplot(312)
    ax.set_title('Sterowanie')
    ax.scatter(t, steering, color='g')

    ax = plt.subplot(313)
    ax.set_title('Blad')
    ax.plot(t, error, color='r')

    plt.show()


if __name__ == '__main__':
    make_simulation()
