# coding=utf-8

import sys
import warnings
import numpy as np
import time

# My own lib for mathematics
# Моя библиотека для работы с мат. функциями
# TODO Rename
import powerful_lib as pl

# Constants
# Константы
accuracy = 0.1 ** 5

# Coefficients before x of functions
# Коэффициенты перед иксами функции
coefficients = [1, -3, 0, 3]


# Function of x and constants
# Функция от x и констант
def f(x, a=coefficients):
    result = 0
    power = len(a)

    for n in range(0, power):
        result += a[n] * x ** (power - n - 1)

    return result


# Polynomial
# Полином
def poly(x, a):
    result = 0
    length = len(x)

    for n in range(length):
        result += x[n] * a[n]

    return -result


def bernoulli_method(xn, an, iterations):
    x = poly(xn, an)

    # if abs(f(x / xn[0], coefficients)) <= accuracy:
    if iterations > 10:
        return [x / xn[0], iterations, f(x / xn[0], coefficients)]
    else:
        # x = poly([a, b, c], [])
        #
        # if abs(f(x / a)) <= accuracy:
        #     return [x / a, iterations, f(x / a)]
        #
        # return bernoulli_method(x, a, b, iterations + 1)
        print(x / xn[0], f(x / xn[0], an))

        xn[0] = x
        return bernoulli_method(xn, an, iterations + 1)


if __name__ == "__main__":
    pl.build_function_x(f,
                        0.01,
                        "Первая функция системы",
                        -5, 5, -5, 5,
                        [1, -3, 0, 3]
                        )

    pl.show_plot()

    print(bernoulli_method([1, 2, 3], coefficients, 0))

    # mpl.bar_chart(
    #     [20, 35, 30, 35, 27],
    #     ["Бернули", "test 2", "test 3", "test 4", "test 5"],
    #     "Производительность",
    #     "Методы",
    #     "Миллисекунды",
    #     graph_params=[0, 51, 5]
    # )

    # start = time.time()
    # end = time.time()
    # print('{:f}'.format(end - start))
