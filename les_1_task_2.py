# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 1 task 2
# October 2019

# task:	Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#       Используйте форматирование строк.

# Solution:
time_sec = int(input("Введите время в секундах (от 0 до 86400): "))
hours = time_sec // 3600
minutes = (time_sec - hours * 3600) // 60
seconds = (time_sec - hours * 3600) % 60
# print(f"{time_sec} секунд соответствует {hours}:{minutes}:{seconds}")
print(f"{time_sec} секунд соответствует {hours:02d}:{minutes:02d}:{seconds:02d}")
