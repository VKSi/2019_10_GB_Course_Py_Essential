# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 5 task 3
# October 2019

# task: 3)	Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#       Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#       Выполнить подсчет средней величины дохода сотрудников.

# Solution:


def task_3():
    wages = {}
    try:
        with open('task_3.txt', 'r', encoding='utf-8') as file:
            for line in file:
                wages[line.split()[0]] = float(line.split()[1])
        print('Меньше 20000 получают:')
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)}')
    except IOError:
        print('Бухгалтер сбежал с ведомостью. Зарплаты не будет')
    except:
        print('Что-то пошло не так')


task_3()
print('Итого как всегда меньше всех работал и больше всех получает )))')
