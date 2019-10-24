# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 5 task 7
# October 2019

# task: 7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
#       данные о фирме: название, форма собственности, выручка, издержки.
#       Пример строки файла: firm_1   ООО   10000   5000.
#       Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#       Если фирма получила убытки, в расчет средней прибыли ее не включать.
#       Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
#       со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#       Пример списка: [{‘firm_1’: 5000, ‘firm_2’: 3000, ‘firm_3’: 1000}, {‘average_profit’: 2000}].
#       Итоговый список сохранить в виде json-объекта в соответствующий файл.
#       Подсказка: использовать менеджер контекста.

# Solution:
import json


def task_7():
    data = [{}, {}]
    data[1]['average_profit'] = 0
    try:
        with open('task_7.txt', 'r', encoding='utf-8') as file:
                file.readline()  # Пропускаем заголовочную строку
                num = 0
                for line in file:
                    print(line.split())
                    num += 1
                    name = line.split()[0]
                    profit = float(line.split()[2]) - float(line.split()[3])
                    data[0][name] = profit
                    data[1]['average_profit'] += profit
                data[1]['average_profit'] /= profit
    except IOError:
        print('Ошибка работы с исходным файлом данный')
    except:
        print('Что-то пошло не так')

    try:
        with open('task_7.json', 'w') as j_file:
            json.dump(data, j_file)
    except IOError:
        print('Ошибка записи в файл')


task_7()
