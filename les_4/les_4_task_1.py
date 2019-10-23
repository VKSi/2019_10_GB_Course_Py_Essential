# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 4 task 1
# October 2019

# task: 1)	Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#       В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
#       Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# Solution:
from sys import argv

script_name, productivity, hourly_rate, bonus = argv

print('-' * 30)
print(f'Productivity : {productivity:>15}')
print(f'Hourly rate  : {hourly_rate:>15}')
print(f'Bonus        : {bonus:>15}')
try:
    print(f'Wage         : {float(productivity) * float(hourly_rate) + float(bonus):>15}')
except ValueError:
    print('Кто вводит левые значения, остается без зарплаты.')
print('-' * 30)
