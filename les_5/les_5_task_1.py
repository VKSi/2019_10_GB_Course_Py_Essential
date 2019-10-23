# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 5 task 1
# October 2019

# task: 1)	Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#       Об окончании ввода данных свидетельствует пустая строка.

# Solution:


def task_1():
    try:
        with open("task_1.txt", 'a', encoding='utf-8') as file:
            while True:
                my_line = input('Введите новую строку: ')
                if my_line == '':
                    break
                file.write(my_line + '\n')
    except IOError:
        print('Ошибка при работе с файлом')
    except:
        print("Извините, что-то пошло не так")
    finally:
        print('Работа программы завершена.')


task_1()
