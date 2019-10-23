# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 5 task 4
# October 2019

# task: 4)	Создать (не программно) текстовый файл со следующим содержимым:
#       One — 1
#       Two — 2
#       Three — 3
#       Four — 4
#       Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#       При этом английские числительные должны заменяться на русские.
#       Новый блок строк должен записываться в новый текстовый файл.

# Solution:


def task_4():
    en_rus = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
    new_lines = []
    try:
        with open('task_4.txt', 'r', encoding='utf-8') as init_f:
            for line in init_f:
                new_lines.append(en_rus[line.split(' ', 1)[0]] + ' '+ line.split(' ', 1)[1])
    except IOError:
        print('Ошибка при работе с исходным файлом')
    try:
        with open('task_4_new.txt', 'a', encoding='utf-8') as new_f:
            new_f.writelines(new_lines)
    except IOError:
        print('Ошибка при работе с конечным файлом')


task_4()
