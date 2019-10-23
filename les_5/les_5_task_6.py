# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 5 task 6
# October 2019

# task: 6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
#       и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
#       Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#       Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
#       Вывести словарь на экран.

# Solution:


def task_6():
    my_dict = {}
    try:
        with open('task_6.txt', 'r', encoding='utf-8') as file:
            for line in file:
                s_line = line.split(':', 1)
                my_dict[s_line[0]] = 0
                line_num = [(x, x[:-1])[x[-1] == ','] for x in s_line[1].split()]  # Убираем запятые, если они есть
                for x in line_num:
                    try:
                        my_dict[s_line[0]] += int(x)
                    except ValueError:
                        continue
                    except:
                        print('Что-то пошло не так')
    except IOError:
        print('Ошибка при работе с файлом')
    print(my_dict)


task_6()
