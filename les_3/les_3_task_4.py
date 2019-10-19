# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 3 task 4
# October 2019

# task: 4)	Программа принимает действительное положительное число x и целое отрицательное число y.
#       Необходимо выполнить возведение числа x в степень y.
#       Задание необходимо реализовать в виде функции my_func(x, y).
#       При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Solution:


def my_func(x, y):
    res = 1
    try:
        for _ in range(abs(y)):
            res /= x
    except ZeroDivisionError:
        print('x должно быть положительным')
    return res


my_x = float(input("Введите действительное положительное число x: "))
my_y = int(input("Введите целое отрицательное число y: "))
if my_x > 0 and my_y < 0:
    print(f'Результат возведения {my_x} в степень {my_y} = {my_func(my_x, my_y):0.4f}')
else:
    print('Проверьте правильность ввода')
