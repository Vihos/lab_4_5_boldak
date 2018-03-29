# coding=utf-8

import sys
import time
import warnings
import numpy as np
import matplotlib.pyplot as plt

# Constants
# Константы
accuracy = 0.1 ** 5
# Промежутки отрисовки функции
START_X = -2
END_X = 2
START_Y = -2
END_Y = 2

# Coefficients of a polynomial
# Коэффициенты полинома
coefficients = [1, 3, -24, 10]


# The polynomial at the point
# Полином в точке
def f(point, a=coefficients):
    result = 0
    power = len(a)

    for n in range(0, power):
        result += a[n] * point ** (power - n - 1)

    return result


# Разностное уравнение (из полинома выражаем х в максимальной степени)
# При каждом вызове нужно сместить коэффициенты приближения
# TODO Rename
def x_max_degree(_coefficients, _approximation):
    # print(_approximation)
    # print(_coefficients)
    result = 0
    length = len(_approximation)

    for n in range(length):
        # print(n)
        result += _approximation[n] * _coefficients[n + 1]

    return -result / _coefficients[0]


# принимает: начальное приближение, коэффициенты, номер итерации
# возращает: корень и количество итераций, за которое он найден
def bernoulli_approximation(_coefficients, _approximation, _iteration):
    x_last = x_max_degree(_coefficients, _approximation)
    max_root = x_last / _approximation[0]

    if abs(f(max_root)) <= accuracy:
        return max_root, _iteration
    else:
        _approximation = [x_last] + _approximation[:-1]
        return bernoulli_approximation(_coefficients, _approximation, _iteration + 1)


# принимает: коэффициенты полинома, корень
# возращает: новые коэффициенты полинома
def gornor_schema(_coefficients, root):
    new_coefficients = [_coefficients[0]]

    length = len(_coefficients) - 2

    for n in range(length):
        new_coefficients.append(root * new_coefficients[n] + _coefficients[n + 1])

    return new_coefficients


# 2 steps: 1) approximation of max|root| 2) creation new polynomial coefficients
# принимает: начальное приближение, коэффициенты
def bernoulli_method_interface(_coefficients, _approximation):
    roots = []
    iterations = []
    length = len(_approximation)

    for k in range(length):
        # 1) approximation of max|root|
        temp = bernoulli_approximation(_coefficients, _approximation, 0)

        roots.append(temp[0])
        iterations.append(temp[1])

        # 2) creation new polynomial coefficients
        _coefficients = gornor_schema(_coefficients, temp[0])
        _approximation.remove(_approximation[0])    # delete one approximation
    return roots, iterations


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


if __name__ == "__main__":
    build_function(f,
                   coefficients,
                   "Первая функция системы",
                   -10, 10, -20, 100,
                   0.01,
                   )

    show_plot()

    print(bernoulli_method_interface(coefficients, [1, 2, 3]))

    # mpl.bar_chart(
    #     [20, 35, 30, 35, 27],
    #     ["Бернулли", "test 2", "test 3", "test 4", "test 5"],
    #     "Производительность",
    #     "Методы",
    #     "Миллисекунды",
    #     graph_params=[0, 51, 5]
    # )

    # start = time.time()
    # end = time.time()
    # print('{:f}'.format(end - start))
