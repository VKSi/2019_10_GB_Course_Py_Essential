# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 5 task 2
# October 2019

# task: 2)	Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
#       количества слов в каждой строке.

# Solution:


def task_2():
    try:
        with open('task_2.txt', 'r', encoding='utf-8') as file:
            my_lines = file.readlines()
            for i, my_line in enumerate(my_lines, 1):
                my_line = my_line[:-2]  # Отрезаем перенос строки
                if len(my_line):
                    words_num = (1, 0)[my_line[0] == ' ']  # Если в начале строки пробел, счетчик равен нулю
                    for j in range(len(my_line)):
                        if words_num == 0 and my_line[j] == ' ': # Не обращаем внимание на начальные пробелы
                            continue
                        if my_line[j - 1] == ' 'and my_line[j] != ' ':
                            words_num += 1
                    print(f'В строке № {i} {words_num} слов(а)')
                else:
                    print(f'Строка {i} пустая')
            print(f'В файле {i} строк')
    except IOError:
        print('Ошибка при работе с файлом')
    except:
        print('Что-то пошло не так')


task_2()
