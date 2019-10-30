# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 7 task 1
# October 2019

# task: 1)	Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__() ),
#       который должен принимать данные (список списков) для формирования матрицы.
#       Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#       Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#       Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
#       (двух матриц). Результатом сложения должна быть новая матрица.
#       Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
#       складываем с первым элементом первой строки второй матрицы и т.д.

# Assumption: Задача решена для целочисленных значений, как показано в примере
# Solution:


class Matrix:
    def __init__(self, matrix):
        try:
            for row in matrix:
                for el in row:
                    _ = int(el)
        except ValueError:
            print('Only integer values are expected!')
        self.matrix = matrix

    def __str__(self):
        my_str = '\n'
        for row in self.matrix:
            for el in row:
                my_str += f'{el:>10}'
            my_str += '\n'
        return my_str

    def __add__(self, other):
        add = []
        try:
            if len(self.matrix) != len(other.matrix):
                raise NameError('WrongDimensions')
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    raise NameError('WrongDimensions')
                row = []
                for j in range(len(self.matrix[i])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                add.append(row)
        except NameError:
            print('Please check matrixes dimensions')
            return None
        return Matrix(add)


my_m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f'my_m1 = {my_m1}')
my_m2 = Matrix([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print(f'my_m2 = {my_m2}')
print(f'my_m1 + my_m2 = {my_m1 + my_m2}')
