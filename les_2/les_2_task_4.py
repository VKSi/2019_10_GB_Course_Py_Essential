# GeekBrains Courses. Python Essential
# Vasilii Sitdikov
# Lesson 2 task 4
# October 2019

# task: 4)	Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
#           слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить
#           только первые 10 букв в слове.

# Solution:
my_tuple = input('Введите строку из нескольких слов, разделенных пробелами: ').split(' ')

for i, word in enumerate(my_tuple, 1):
    print(f'{i} {word[:10]}')
