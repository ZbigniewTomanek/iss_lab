from matplotlib import pyplot
import numpy as np


def water_sim():

    """
    To są stałe zdefiniowane przy wyprowadzaniu wzorów, a to stała proporcjonalności,
     T to całkowity czas trwania symulacji a h to moment czasu, co jaki liczymy aprokymację funkcji ze wzoru
     xi+1 = xi + a * xi' * h ,
     x0 = jakaś założona wartość początkowa, w tym wypadku temperatura 100 stopni dla stygnącej wody

     Dla tego modelu założylismy x'(t) = -ax
    """
    a = 1
    T = 10
    h = 0.001  # rzekomo najczęściej używana jest wartość 0.01
    x0 = 100

    # Tutaj wypełniamy tablicę wszystkimi rozpatrywanymi momentami czasu
    t = [i * h for i in range(int(T/h))]

    # Inicjujemy tablicę, która będzie przechowywała wartości temperatury o tej samej długości, co t
    x = [x0] * len(t)

    # No i tu dzieje się cała aproksymacyjna magia
    for i in range(1, len(t)):
        x[i] = x[i - 1] - a * h * x[i - 1]

    # na koniec robimy z tego pierdolony wykres, najlepiej ogarnąć tworzenie paru lini na jednym wykresie,
    # zmianę kolorów i podpis osi
    pyplot.plot(t, x, 'bo')
    pyplot.show()


if __name__ == '__main__':
    water_sim()
