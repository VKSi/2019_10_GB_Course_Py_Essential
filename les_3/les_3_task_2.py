# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 3 task 2
# October 2019

# task: 2)	Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#       имя, фамилия, год рождения, город проживания, email, телефон.
#       Функция должна принимать параметры как именованные аргументы.
#       Реализовать вывод данных о пользователе одной строкой.

# Solution:

def print_info(name, surname, b_year, city, email, phone_number):
    print(f'Имя: {name}, Фамилия: {surname}, год рождения: {b_year}, '
          f'город проживания: {city}, e-mail: {email}, телефон: {phone_number}')


print_info(name='Гена', surname='Крокодил', b_year=1966, city='Ленинград', email='Gena@croc.usp', phone_number='Будка')
