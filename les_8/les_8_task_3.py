# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 8 task 3
# October 2019

# task: 3)	Создайте собственный класс-исключение, который должен проверять содержимое списка на отсутствие элементов
#       типа строка и булево. Проверить работу исключения на реальном примере.
#       Необходимо запрашивать у пользователя данные и заполнять список.
#       Класс-исключение должен контролировать типы данных элементов списка.


# Solution:
class MyEx(Exception):
    def __init__(self, txt, lst):
        super().__init__(txt)
        self.input = lst
        self.txt = txt


def checkargs(lst):
    for el in lst:
        print(el)
        if type(el) == bool:
            raise MyEx(f'There is some "bool" value "{el}"', lst)
        elif type(el) == str:
            raise MyEx(f'There is some "str" value {el}', lst)


def trier(lst):

    try:
        checkargs(lst)
    except MyEx as err:
        print(err.txt)


# Пока реализовано так. Не очень понятно, что имелось ввиду в задании.
# Получая значения от пользователя через input мы всегда будем иметь строковые данные.
my_list = [1, 2.0, True, 'text']
trier(my_list)
my_list = [1, 2.0, 'text', True]
trier(my_list)
