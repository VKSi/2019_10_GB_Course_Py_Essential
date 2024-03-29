# coding=utf-8
# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 1 task 5
# October 2019

# task:	Запросите у пользователя значения выручки и издержек фирмы.
#       Определите, с каким финансовым результатом работает фирма (прибыль - выручка больше издержек
#       или убыток - издержки больше выручки). Выведите соответствующее сообщение.
#       Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
#       Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# Solution:
revenue = float(input("Введите значение выручки (тугрики) - "))
costs = float(input("Введите значение издержек (тугрики) - "))
result = revenue - costs
if result > 0:
    print(f"Поздравляю! Ваша компания работает с прибылью {result:.2f} тугриков!")
    print(f"Рентабельность выручки составила {result / revenue:.3f}")
    personal_n = int(input("Сколько счастливых целочисленных сотрудников работает в Вашей компании? "))
    print(f"Если Вы раздадите прибыль компании сотрудникам, то каждый получит по {result / personal_n:.2f} тугриков.")
elif result < 0:
    print(f"Увы, Ваша компания пока сработала с убытком {-result} тугриков! Старайтесь, у Вас все получится!")
else:
    print(f"Ноль - это тоже хороший результат! Попросите у друга тугрик и пропейте его вместе за стабильность!")
