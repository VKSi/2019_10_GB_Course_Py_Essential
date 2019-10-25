# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 6 task 1
# October 2019

# task: 1)	Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
#       и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора
#       в режимы: красный, желтый, зеленый. Время перехода между режимами должно составлять 7 и 2 секунды.
#       Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Solution:
from time import time, ctime
from itertools import cycle


class TrafficLight:
    __color = 'red'

    def running(self):
        colors = cycle(['red', 'yellow', 'green', 'yellow'])
        self.__color = next(colors)
        start_time = time()
        switch_time = time()
        print(f'Now is {ctime()}, Color: {self.__color}')
        while time() < start_time + 60:
            # Switch from yellow in 2 seconds, otherwise in 7 seconds
            if (time() > switch_time + 7, time() > switch_time + 2)[self.__color == 'yellow']:
                switch_time = time()
                self.__color = next(colors)
                print(f'Now is {ctime()}, Color: {self.__color}')


my_tl = TrafficLight()
my_tl.running()
