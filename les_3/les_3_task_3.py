# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 3 task 3
# October 2019

# task: 3)	Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#           и возвращает сумму наибольших двух аргументов.

# Solution:


def my_func(a, b, c):
    if a <= b <= c:
        return b + c
    elif b <= c <= a:
        return c + a
    else:
        return a + b


def my_func_2(a, b, c):
    my_list = sorted([a, b, c])
    return sum(my_list[1:])

