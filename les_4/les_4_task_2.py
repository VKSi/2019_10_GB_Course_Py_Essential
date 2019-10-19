# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 4 task 2
# October 2019

# task: 2)	Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
#       предыдущего элемента.
#       Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
#       Для формирования списка использовать генератор.

# Solution:


def new_list(old_list):
    try:
        return [old_list[i] for i in range(1, len(old_list)) if old_list[i] > old_list[i - 1]]
    except TypeError:
        print('Check type of values')


def test():
    my_list = [1, 2, -30, 60, 50, 345]
    print(new_list(my_list))


test()
