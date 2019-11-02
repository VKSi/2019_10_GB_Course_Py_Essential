# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 8 task 1
# October 2019

# task: 1)	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
#       «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
#       должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
#       должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#       Проверить работу полученной структуры на реальных данных.

# Solution:
import datetime
# Примечание: какая-то странная и бесмыссленная задачка, совсем как русский бунт.
# Зачем в классе инициализировать дату, если дальше использовать методы, не имеющие доступа к объекам класса?


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extractor(cls, d):
        if Date.validator(d):
            return datetime.date(int(d[6:]), int(d[3:5]), int(d[:2]))
        else:
            print('Check the format of date')

    @staticmethod
    def validator(d):
        try:
            datetime.date(int(d[6:]), int(d[3:5]), int(d[:2]))
            return True
        except ValueError:
            return False


print(Date.extractor('01-11-2019'))
print(Date.validator('01-11-2019'))
print(Date.extractor('01-13-2019'))
print(Date.validator('01-13-2019'))
