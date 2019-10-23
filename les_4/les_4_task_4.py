# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 4 task 4
# October 2019

# task: 4)	Представлен список чисел. Определить элементы списка, не имеющие повторений.
#       Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в
#       порядке их следования в исходном списке.
#       Для выполнения задания обязательно использовать генератор.

# Solution:


def unique_els(the_list):
    new_list = [x for x in the_list if the_list.count(x) == 1]
    return new_list
