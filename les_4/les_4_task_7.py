# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 4 task 7
# October 2019

# task: 7) Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#       При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
#       for el in fibo_gen().
#       Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
#       Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24

# Solution:
from itertools import count


# Название изменено с fibo_gen(), видимо оставшегося от задачи подсчета чисел Фибоначчи на factor_gen()
def factor_gen():
    res = 1  # Для ускорения работы значение факториала будем меморезировать
    for n in count(1):
        res *= n
        yield res


def factor_15():
    counter = 0
    for el in factor_gen():
        counter += 1
        if counter <= 15:
            print(f'{counter}! = {el}')
        else:
            break


factor_15()
