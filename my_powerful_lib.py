import numpy as np
import matplotlib.pyplot as plt

# Точность
accuracy = 0.00001

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
def build_function_x(func, dx=0.01, legend="", x_from=START_X, x_to=END_X):
    plt.axis([START_X, END_X, START_Y, END_Y])
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    x = np.arange(x_from, x_to, dx)

    if len(legend) > 0:
        plt.plot(x, func(x), label=legend)
        plt.legend()
    else:
        plt.plot(x, func(x))


# Строит график неявно заданной функцию f(x,y) = 0
# func - функция принимающая 2 параметра x, y
# dx - шаг, Стандартно 0.01
# legend - подпись
# move - сдвигать ли подпись на 0.01 по обеим осям
# l_x, l_y - кординаты для подписи, если нужны свои
# Лучше указвыать статичные координаты т.к функция автопоиска не всегда работает корректно
# l_color - цвет фона надписи, стандартно прозрачный
# x_from, y_from - начало отрисовки функции
# x_to, y_to - конец отрисовки функции
def build_function_xy(func, dx=0.01, legend="", move=True, legend_x=0, l_x=None, l_y=None, l_color="", x_from=START_X,
                      x_to=END_X, y_from=START_Y, y_to=END_Y):
    plt.axis([START_X, END_X, START_Y, END_Y])
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    x_array = np.arange(x_from, x_to, dx)
    y_array = np.arange(y_from, y_to, dx)

    if move:
        move_ = 0.01
    else:
        move_ = 0

    if len(legend) > 0 and l_x is None and l_y is None and not is_nan(func(0, 0)):
        l_x = legend_x + move_

        if legend_x > 0:
            l_y = -func(legend_x, 0) + move_
        else:
            l_y = -func(legend_x, legend_x) + move_

    else:
        l_x = 0
        l_y = 0

    x, y = np.meshgrid(x_array, y_array)
    f = func(x, y)

    plt.contour(x, y, f, [0])

    if len(legend) > 0:
        if len(l_color) > 0:
            plt.annotate(legend, (l_x, l_y), backgroundcolor=l_color)
        else:
            plt.annotate(legend, (l_x, l_y))


# Отрисовывает функции которые были построены через 'build_function_x(...)' и 'build_function_xy(...)'
def show_plot():
    plt.show()


# Находит первые точки в которых существует функция (слева и справа) на заданом промежутке
# Применимо только к f(x)
# [a, b] - промежуток
# Выкидывает Exception в случаи если функция не существует на данном промежутке
def find_func(a, b, _accuracy = 0.1):
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
