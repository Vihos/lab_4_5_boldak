# ================================================================ #
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
import time

# My own lib for mathematics
import my_powerful_lib as mpl

# Коэффициенты перед иксами функции
a0, a1, a2, a3 = 1, -3, 0, 3


# Функция
def f2(x, y):
    return np.cos(y - 1) + x - 0.7


if __name__ == "__main__":
    mpl.build_function_xy(f2, 0.01, "Первая функция системы")
    mpl.show_plot()

    # mpl.bar_chart(
    #     [20, 35, 30, 35, 27],
    #     ["Бернули", "test 2", "test 3", "test 4", "test 5"],
    #     "Производительность",
    #     "Методы",
    #     "Миллисекунды",
    #     graph_params=[0, 51, 5]
    # )
    #
    # start = time.time()
    # time.sleep(1)
    # end = time.time()
    # print('{:f}'.format(end - start))
