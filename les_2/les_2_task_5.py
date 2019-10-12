# GeekBrains Courses. Python Essential
# Vasilii Sitdikov
# Lesson 2 task 5
# October 2019

# task: 5)	Реализовать структуру «Р ейтинг» , представляющую собой не возрастающий набор
#       натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в
#       рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
#       значением должен разместиться после них.
#       Подсказка.
#       Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#       Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3 , 2.
#       Пользователь ввел число 8. Результат: 8 , 7, 5, 3, 3, 2.
#       Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1 .
#       Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

# Solution:
my_list = []
while True:
    value = int(input('Введите любое натуральное число (для прекращения работы введите отрицательное число): '))
    if value < 0:  # Отработка выхода из программы
        break
    if not my_list:  # Отработка ввода первого значения
        my_list.append(value)
    elif value <= my_list[-1]:  # Отработка добавления минимального значения в конец
        my_list.append(value)
    else:  # Отработка поиска места для нового значения
        for i in range(len(my_list)):
            if value <= my_list[len(my_list) - i - 1]:
                my_list.insert(len(my_list) - i, value)
                break
        else:  # Отработка добавления максимального значения в начало
            my_list.insert(0, value)
    print(f'Текущее состояние списка: \n{my_list}')