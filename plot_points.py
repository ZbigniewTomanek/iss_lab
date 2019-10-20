from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as stats


def sin():
    x = np.arange(0, 10, 0.2)
    y1 = np.sin(x)
    y2 = np.cos(x)

    fig, ax = plt.subplots()

    ax.set_xlabel('arg')
    ax.set_ylabel('val')

    ax.plot(x, y1, label='sinus', marker='x')
    ax.plot(x, y2, label='cosinus', marker='o')

    plt.title('Funkcje trygonometryczne')
    plt.legend()
    plt.show()


def normal_distr():
    y = np.random.normal(loc=0, size=50)
    fig, ax = plt.subplots()
    ax.scatter(np.arange(50), y)

    plt.title('Normal distribution')
    plt.show()


def random_points():
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    plt.scatter(x, y)
    plt.show()


def plot_gaussian_curve():
    mu = 0
    variance = 1
    sigma = np.sqrt(variance)

    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma))
    plt.show()


def euler(x0, delta, a):
    x = np.linspace(x0, x0 + delta)
    plt.plot(x, a * np.exp(a * x))
    plt.show()


if __name__ == '__main__':
    euler(5, 10, -0.2)
