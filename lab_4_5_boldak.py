# ================================================================ #
#                                                                  #
# Лабораторная работа #4-5                                         #
# Работу выполнил Болдак Дмитрий Алексеевич                        #
#                                                                  #
#                                                                  #
# Проект сделан на Python 3.6                                      #
# Инструкция по установке пакетов для Linux                        #
#                                                                  #
# $ sudo pip3 install matplotlib==2.1.0                            #
# $ sudo pip3 install numpy                                        #
# $ sudo pip3 install scipy                                        #
#                                                                  #
# ================================================================ #
import sys
import warnings
import numpy as np
from scipy.misc import derivative

# Моя библиотека для удобного построения графиков и не только
import powerful_lib as mpl

# Константы
accuracy = 0.00001


# Функция
def f1(x, y):
    return np.sin(x) + 2 * y - 2


def f2(x, y):
    return np.cos(y - 1) + x - 0.7


def f3(x, y):
    return np.tan(x * y + 0.1) - x ** 2


def f4(x, y):
    return x ** 2 + 2 * y ** 2 - 1


def _f1(x):
    return 1 - np.sin(x) / 2


def _f2(y):
    return 0.7 - np.cos(y - 1)


# 0 - means derivative with respect to x, 1 - means derivative with respect to y
def diff_f(func, var=0, point=None):
    if point is None:
        point = []
    args = point[:]

    def wraps(x):
        args[var] = x
        return func(*args)

    return derivative(wraps, point[var], dx=1e-6)


def iteration(x0, y0, __f1, __f2, n):
    if abs(f1(x0, y0)) < accuracy and abs(f2(x0, y0)) < accuracy:
        return [x0, y0, f1(x0, y0), f2(x0, y0), n]
    else:
        y = __f1(x0)
        x = __f2(y0)

        return iteration(x, y, __f1, __f2, n + 1)


def newton_piston(x0, y0, _f1, _f2, n):
    if abs(_f1(x0, y0)) < accuracy and abs(_f2(x0, y0)) < accuracy:
        return [x0, y0, _f1(x0, y0), _f2(x0, y0), n]
    else:

        detJ = diff_f(_f1, 0, [x0, y0]) * diff_f(_f2, 1, [x0, y0]) - diff_f(_f1, 1, [x0, y0]) * diff_f(_f2, 0, [x0, y0])
        detA1 = _f1(x0, y0) * diff_f(_f2, 1, [x0, y0]) - diff_f(_f1, 1, [x0, y0]) * _f2(x0, y0)
        detA2 = diff_f(_f1, 0, [x0, y0]) * _f2(x0, y0) - _f1(x0, y0) * diff_f(_f2, 0, [x0, y0])

        x = x0 - detA1 / detJ
        y = y0 - detA2 / detJ

        return newton_piston(x, y, _f1, _f2, n + 1)


def print_result(x, y, f1, f2, n):
    temp_x_e = str("%.2e" % x)
    temp_x_f = str("%.6f" % x)
    temp_y_e = str("%.2e" % y)
    temp_y_f = str("%.6f" % y)

    temp_iterations = str(n)

    temp_f1_x_e = str("%.2e" % f1)
    temp_f1_x_f = str("%.6f" % f1)
    temp_f2_x_e = str("%.2e" % f2)
    temp_f2_x_f = str("%.6f" % f2)

    print(
        ("Корень системы нелинейных уравнений: x = {0} ({1}), y = {2} ({3})\n" +
         "Найдены за {4} итерации(ий) \n" +
         "Функции в этих точках: f1(x,y) = {5} ({6}) <= {9}  (точность); f2(x,y) = {7} ({8}) <= {9} (точность)").format(
            temp_x_e, temp_x_f, temp_y_e, temp_y_f,
            temp_iterations,
            temp_f1_x_e, temp_f1_x_f, temp_f2_x_e, temp_f2_x_f,
            accuracy
        )
    )


if __name__ == "__main__":
    # Отключение вывода некоторых уведомлений
    if not sys.warnoptions:
        warnings.simplefilter("ignore")

    # Устанавливает максимальную глубину рекурсии на 2000
    sys.setrecursionlimit(5000)

    # нарисуем функцию и её производной на промежутке заданном впараметрах проагрммы сверху
    # mpl.build_function_xy(f1, 0.01, "Первая функция системы", "blue")
    # mpl.build_function_xy(f2, 0.01, "Вторая функция системы")
    # mpl.show_plot()

    mpl.build_function_xy(f3, 0.01, "Первая функция системы", "blue")
    mpl.build_function_xy(f4, 0.01, "Вторая функция системы")
    mpl.show_plot()

    # try:
    #     print("Метод итерации:")
    #     temp = iteration(0, 0, _f1, _f2, 0)
    #     print_result(temp[0], temp[1], temp[2], temp[3], temp[4])
    # except Exception as e:
    #     print(e)
    #
    # print()
    #
    # try:
    #     print("Метод ньютона:")
    #     temp = newton_piston(-1, -1, f1, f2, 0)
    #     print_result(temp[0], temp[1], temp[2], temp[3], temp[4])
    # except Exception as e:
    #     print(e)

    # print()

    try:
        print("Метод ньютона #1:")
        temp = newton_piston(-1, -1, f3, f4, 0)
        print_result(temp[0], temp[1], temp[2], temp[3], temp[4])
        print()
        print("Метод ньютона #2:")
        temp = newton_piston(-1, 1, f3, f4, 0)
        print_result(temp[0], temp[1], temp[2], temp[3], temp[4])
        print()
        print("Метод ньютона #3:")
        temp = newton_piston(1, -1, f3, f4, 0)
        print_result(temp[0], temp[1], temp[2], temp[3], temp[4])
        print()
        print("Метод ньютона #4:")
        temp = newton_piston(1, 1, f3, f4, 0)
        print_result(temp[0], temp[1], temp[2], temp[3], temp[4])
        print()
    except Exception as e:
        print(e)
