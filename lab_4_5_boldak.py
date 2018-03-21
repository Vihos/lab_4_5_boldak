# ================================================================ #
#                                                                  #
# Лабораторная работа #2                                           #
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

# My own lib for mathematics
import my_powerful_lib as mpl


# Функция
def f1(x):
    return 1 - np.sin(x) / 2


def f2(x, y):
    return np.cos(y - 1) + x - 0.7


if __name__ == "__main__":
    # Отключение вывода некоторых уведомлений
    if not sys.warnoptions:
        warnings.simplefilter("ignore")

    # Устанавливает максимальную глубину рекурсии на 2000
    sys.setrecursionlimit(500)

    # нарисуем функцию и её производной на промежутке заданном впараметрах проагрммы сверху
    mpl.build_function_x(f1, 0.01, "Первая функция системы")
    mpl.build_function_xy(f2, 0.01, "← Вторая функция системы", legend_x=0.5)
    mpl.show_plot()

    print(f2(0.5, 1))
