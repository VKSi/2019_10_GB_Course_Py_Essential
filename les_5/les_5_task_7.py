# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 5 task 7
# October 2019

# task: 7)	Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
#       название, форма собственности, выручка, издержки.
#       Необходимо вычислить прибыль каждой компании и среднюю прибыль.
#       Реализовать список, содержащий словарь (название фирмы и прибыль) и словарь с одним элементом (средняя прибыль).
#       Добавить в первый словарь еще один элемент, содержащий результат вычисления отношения прибыли к убыткам.
#       Итоговый список сохранить в файл.

# Solution:


def task_7():
    data = []
    with open('task_7.txt', 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            print(line.split())
            name = line.split()[1] + ' ' + line.split()[0]
            profit = float(line.split()[2]) - float(line.split()[3])

            data.append({name : profit})
    print(data)


task_7()
