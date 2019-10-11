# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 1 task 1
# October 2019

# task: 1)	Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
#           несколько чисел и строк и сохраните в переменные, выведите на экран.

# Solution:

# 1. Creation
int_variable = 1
float_variable = 3.1415926
string_variable = "Good morning, Maria!"
bool_variable = True

# 2. Output
print(string_variable)
print(f"I've prepared my {int_variable} code for your.")
print(f"Is p = {float_variable}? {bool_variable}")

# 3. Input +
time = int(input("What time do you usually get up (hour)? "))
drink = input("What is your favorite morning drink? ")
print(f"\n It's {time} o'clock now! Get up and drink your {drink}!")
