import numpy as np
import matplotlib.pyplot as plt

# Точность
accuracy = 10 ** -5

# Промежуткиы отрисовки функции
START_X = -2
END_X = 2
START_Y = -2
END_Y = 2


# Проверка является ли значение функции бесконечностью
def is_nan(arg):
    return arg != arg


# Строит функцию f(x)
# func - функция принимающая 1 параметр x
# dx - шаг, Стандартно 0.01
# legend - подпись
# x_from - начало отрисовки функции
# x_to - конец отрисовки функции
def build_function_x(func, dx=0.01, legend="", x_from=START_X, x_to=END_X, y_from=START_Y, y_to=END_Y, argument=None):
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


# Строит график неявно заданной функцию f(x,y) = 0
# func - функция принимающая 2 параметра x, y
# dx - шаг, Стандартно 0.01
# legend - подпись
# color - цвет функции
# x_from, y_from - начало отрисовки функции
# x_to, y_to - конец отрисовки функции
def build_function_xy(func, dx=0.01, legend="", color="", x_from=START_X,
                      x_to=END_X, y_from=START_Y, y_to=END_Y):
    plt.axis([START_X, END_X, START_Y, END_Y])
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    x_array = np.arange(x_from, x_to, dx)
    y_array = np.arange(y_from, y_to, dx)

    x, y = np.meshgrid(x_array, y_array)
    f = func(x, y)

    if len(color) > 0:
        ctr = plt.contour(x, y, f, [0], colors=color)
    else:
        ctr = plt.contour(x, y, f, [0])

    if len(legend) > 0:
        ctr.collections[0].set_label(legend)
        plt.legend(loc="upper right")


# Отрисовывает функции которые были построены через 'build_function_x(...)' и 'build_function_xy(...)'
def show_plot():
    plt.figure()
    plt.show()


# Находит первые точки в которых существует функция (слева и справа) на заданом промежутке
# Применимо только к f(x)
# [a, b] - промежуток
# Выкидывает Exception в случаи если функция не существует на данном промежутке
def find_func(f, a, b, _accuracy=0.1):
    x = np.arange(a, b, _accuracy)

    ret_x_start = None
    ret_x_end = None

    for xn in x:
        temp = f(xn)

        if not is_nan(temp):
            ret_x_start = xn

            break

    for xn in reversed(x):
        temp = f(xn)

        if not is_nan(temp):
            ret_x_end = xn

            break

    if ret_x_start is None or is_nan(ret_x_start) or ret_x_end is None or is_nan(ret_x_end):
        raise Exception('На данном промежутке функция не существует')

    return ret_x_start, ret_x_end


def bar_chart(values_array, values_names=None, title=None, x_title=None, y_title=None, graph_params=None):
    ind = np.arange(len(values_array))
    width = 0.35

    p = plt.bar(ind, values_array, width)

    if title is not None:
        plt.title(title)

    if x_title is not None:
        plt.xlabel(x_title)

    if y_title is not None:
        plt.ylabel(y_title)

    if values_names is not None and len(values_names) == len(values_array):
        plt.xticks(ind, values_names)

    if graph_params is not None and len(graph_params) == 3:
        plt.yticks(np.arange(graph_params[0], graph_params[1], graph_params[2]))

    plt.show()
