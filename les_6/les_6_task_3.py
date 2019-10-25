# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 6 task 3
# October 2019

# task: 3)	Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#       name, surname, position (должность), income (доход).
#       Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
#       оклад и премия, например, {"profit": profit, "bonus": bonus}.
#       Создать класс Position (должность) на базе класса Worker.
#       В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#       и дохода с учетом премии (get_full_profit).
#       Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
#       проверить значения атрибутов, вызвать методы экземпляров).

# Solution:


class Worker:

    def __init__(self, name='Petr', surname='Vasechkin', position='singer', wage=100, bonus=20):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


v_pet = Position('Vasilii', 'Petechkin', 'dancer', 110, 30)
print(f'New attributes are: {v_pet.name}, {v_pet.surname}, {v_pet.position}, {v_pet._income}')
print(f'Total salary of {v_pet.get_full_name()} is {v_pet.get_full_salary()}')
