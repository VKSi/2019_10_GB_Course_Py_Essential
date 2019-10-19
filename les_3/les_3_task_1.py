# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 3 task 1
# October 2019

# task: 1)	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#       Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# Solution:


# Функция:
def div(a, b):
    try:
        res = f'{float(a) / float(b):.2f}'
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'
    except:
        return f'Ну и как я буду делить {a} на {b}?!'
    return res


print(f'Частное = {div(input("Введите делимое: "), input("Введите делитель: "))}')
