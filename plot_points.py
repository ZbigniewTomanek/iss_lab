from matplotlib import pyplot as plt
import numpy as np

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


if __name__ == '__main__':
    sin()