# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 2 task 2
# October 2019

# task: 2)	Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
#       элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
#       сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

# Assumption:
# В задаче не конкретезирован тип элементов списка и не требуется работа с ним. Оставляем строковый тип.

# Solution:
# Создание списка
length = int(input("Задайте длину списка: "))
my_list = []
for i in range(length):
    my_list.append(input(f"Задайте {i + 1}-й элемент списка: "))
print(f'Вами задан список: \n{my_list}')

# Обмен значений
for i in range(1, length, 2):
    my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
print(f'Список после обмена значений: \n{my_list}')
