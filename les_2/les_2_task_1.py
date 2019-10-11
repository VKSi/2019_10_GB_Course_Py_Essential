# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 2 task 1
# October 2019

# task: 1)	Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
#       проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
#       Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# Solution:
# Создание списка
my_list = [1, 2.0, False, 'Guido', ['eggs', 'spam'], range(10),
           {'Gena': 'Crocodile', 'Cheburashka': 'Monster'}, ('tu', 'ple')]

# Проверка типов данных
for item in my_list:
    print(f'Item {item} has a type {type(item)}')
