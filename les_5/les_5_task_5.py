# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 5 task 5
# October 2019

# task: 5)	Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#       Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# Solution:
import random


def task_5(n):
    # n - Количество генерируемых чисел
    # Генерация строки
    my_string = ''
    for i in range(n):
        my_string += f'{random.random() * 100: .2}'
    my_string = my_string[1:]
    print(f'Создана строка: "{my_string}"')

    # Запись строки в файл
    try:
        with open('task_5.txt', 'w') as file:
            file.write(my_string)
    except IOError:
        print('Возникли проблеммы с записью в файл')

    # Чтение строки и подсчет суммы
    try:
        with open('task_5.txt', 'r') as file:
            print(f'Сумма чисел в файле равна: {sum([float(x) for x in file.read().split()])}')
    except IOError:
        print('Возникли проблеммы с чтением из файла')


task_5(10)
