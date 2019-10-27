from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as stats

'''
To jest już kod po modyfikacjach w trakcie zajęć. 
Na sprawdzianie trzeba było wygenerować N przebiegów na jednym wykresie dla funkcji x' = ax i dowolnego parametru a,
gdzie wartości x0 były brane z rozkładu normalnego.
'''


def plot_sims(N=1, T=100, h=0.01):
    mu = 0
    variance = 1
    sigma = np.sqrt(variance)
    x0 = 10
    y0 = 2
    fig, ax = plt.subplots()
    ax.set_xlabel('Stan')
    plt.title('Model lotki-voltery')
    ax.set_ylabel('Wartość')

    gauss = np.random.normal(size=N)

    for i in range(N):
        t, x, y = make_sim(x0, y0, T, h)
        ax.plot(t, x, label='x')
        ax.plot(t, y, label='y')

    plt.legend()
    plt.show()


def make_sim(x0, y0, T, h, a=1, b=1, c=1, d=1):
    t = [(T * (i/T)) for i in range(int(T/h))]
    x = [x0] * len(t)
    y = [y0] * len(t)

    for i in range(1, len(t)):
        x[i] = x[i-1] + h * ((a - b * y[i-1]) * x[i - 1])
        y[i] = y[i-1] + h * ((c * x[i] - d) * y[i - 1])

    t = np.array(t)
    x = np.array(x)
    y = np.array(y)

    return t*h, x, y


if __name__ == '__main__':
    plot_sims()
