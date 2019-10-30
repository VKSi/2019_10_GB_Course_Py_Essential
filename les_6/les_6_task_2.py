# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 6 task 2
# October 2019

# task: 2)	Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#       Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
#       Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
#       Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
#       толщиной в 1 см*число см толщины полотна. Проверить работу метода.
#       Например: 20м*5000м*25кг*5см = 12500 т

# Solution:


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def value(self, weight_ratio, thikness):
        print(f'You need {self._length * self._width * weight_ratio * thikness} kg of asphalt')


my_road = Road(20, 5000)
my_road.value(25, 5)
