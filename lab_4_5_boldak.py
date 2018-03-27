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

# Моя библиотека для удобного построения графиков и не только
import my_powerful_lib as mpl


# Функция
def f1(x):
    return 1 - np.sin(x) / 2


def f2(x, y):
    return np.cos(y - 1) + x - 0.7


def f3(x):
    return np.arccos(0.7 - x) + 1


def f4(x, n=0):
    return np.arccos((-1) ** n * (0.7 - x)) + 1 - n * np.pi


if __name__ == "__main__":
    # Отключение вывода некоторых уведомлений
    if not sys.warnoptions:
        warnings.simplefilter("ignore")

    # Устанавливает максимальную глубину рекурсии на 2000
    sys.setrecursionlimit(500)

    # нарисуем функцию и её производной на промежутке заданном впараметрах проагрммы сверху
    mpl.build_function_x(f1, 0.001, "Первая функция системы")
    # mpl.build_function_x(f3, 0.001, "Первая функция системы")
    # mpl.build_function_x(f6, 0.001, "Первая функция системы")
    mpl.build_function_xy(f2, 0.01, "Вторая функция системы")
    mpl.show_plot()

    print(f2(0.5, 1))
