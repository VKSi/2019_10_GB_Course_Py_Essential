# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 7 task 2
# October 2019

# task: 2)	Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
#       этого проекта — одежда, которая может иметь определенное название.
#       К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
#       размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#       Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
#       для костюма (2*H + 0.3).
#       Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
#       Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
#       проекта, проверить на практике работу декоратора @property .

# Solution:
from abc import ABC, abstractmethod


class Stuff(ABC):
    def __init__(self, param):
        try:
            float(param)
        except ValueError:
            print("Check Parametr's Value")

    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Stuff):
    def __init__(self, param):
        super().__init__(param=param)
        self.size = float(param)
        print(f'There is a new coat with size {self.size}')

    @property
    def get_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Stuff):
    def __init__(self, param):
        super().__init__(param=param)
        self.height = float(param)
        print(f'There is a new suit with height {self.height}')

    @property
    def get_consumption(self):
        return round(self.height * 2 + 0.3, 2 )


my_coat = Coat('48')
print(f'Tissue consumption for my coat is: {my_coat.get_consumption}')
my_suit = Suit('1.78')
print(f'Tissue consumption for my suit is: {my_suit.get_consumption}')
print(f'The total issue consumption is: {my_coat.get_consumption + my_suit.get_consumption}')
