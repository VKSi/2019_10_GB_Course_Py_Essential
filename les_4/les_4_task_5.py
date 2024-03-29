# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 4 task 5
# October 2019

# task: 5) Реализовать формирование списка, используя функцию range() и возможности генератора.
#       В список должны войти четные числа от 100 до 1000 (включая границы).
#       Необходимо получить результат вычисления произведения всех элементов списка.
#       Подсказка: использовать функцию reduce() .

# Solution:
from functools import reduce


def task_5():
    def prod(x1, x2):
        return x1 * x2
    return reduce(prod, [x for x in range(100, 1001) if x % 2 == 0])


print(f'И зачем Вам это число? : {task_5()}')
