import matplotlib.pyplot as plt
import numpy as np

# Промежутки отрисовки функции
START_X = -10
END_X = 10
START_Y = -8
END_Y = 5


# Строит функцию f(x)
# принимает:
# func - функция от одного параметра
# argument - коэффициенты полинома
# legend - подпись
# x_from - начало отрисовки функции по х
# x_to - конец отрисовки функции по х
# y_from - начало отрисовки функции по y
# y_to - конец отрисовки функции по y
# dx - шаг отрисовки, Стандартно 0.01
def build_function(func, argument=None, legend="", x_from=START_X, x_to=END_X, y_from=START_Y, y_to=END_Y, dx=0.01):
    plt.axis([x_from, x_to, y_from, y_to])
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    x = np.arange(x_from, x_to, dx)

    if len(legend) > 0:
        if argument is not None:
            plt.plot(x, func(x, argument), label=legend)
        else:
            plt.plot(x, func(x), label=legend)

        plt.legend()
    else:
        if argument is not None:
            plt.plot(x, func(x, argument))
        else:
            plt.plot(x, func(x))


# Отрисовывает функции, которые были построены через 'build_function(...)'
def show_plot():
    plt.show()
