# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 4 task 6
# October 2019

# task: 6) Реализовать два небольших скрипта:
#           а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
#           б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
#       Подсказка: использовать функцию count() и cycle() модуля itertools .

# Solution:
from itertools import count
from itertools import cycle


# Реализация задачи дословно. Функция возвращает бесконечный итератор:
def my_unf_count(start):
    try:
        return count(start)
    except ValueError:
        print('"start" should be an integer')


# Реализация задачи с ограничением. Функция печатает числа, ничего не возвращает, есть ограничение по максимуму:
def my_count(start, stop=100):
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)


# Реализация задачи дословно. Функция возвращает бесконечный цикл:
def my_inf_cycle(my_list):
    return cycle(my_list)


# Реализация задачи с ограничением. Функция печатает значения, ничего не возвращает, есть ограничение по максимуму:
def my_cycle(my_list, stop=100):
    counter = 0
    for el in cycle(my_list):
        if counter > stop:
            break
        else:
            print(el)
            counter += 1


print('-' * 15)
print(f'Return from my_unf_count(20): {my_unf_count(20)}')
print('-' * 15)
print(f'Return from my_count(20, 30): {my_count(20, 30)}')
print('-' * 15)
print(f'Return from my_inf_cycle([19, True, "GeekBrains"]): {my_inf_cycle([19, True, "GeekBrains"])}')
print('-' * 15)
print(f'Return from my_cycle([19, True, "GeekBrains"], 20): {my_cycle([19, True, "GeekBrains"], 20)}')
