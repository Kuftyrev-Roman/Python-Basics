"""
1)	Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""

class Matrix:
    def __init__(self, args):
        self.args = args

    # def __str__(self):
        # return [f'{self.args[i]}\n{self.args[i]}\n' for i in enumerate(self.args)]

    def __add__(self, other):
        result = [[0 for j in range(len(self.args[0]))] for i in self.args]
        for i in range(len(self.args)):
            for j in range(len(self.args[0])):
                result[i][j] = self.args[i][j] + other.args[i][j]
        return result


a = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[-1, -2, -3], [-4, -5, -6]])
print(a + b)
# print(a)
# print(b)



# class Matrix:
#     def __init__(self, args):
#         self.args = args
#         print(len(self.args))
#     def __str__(self):
#         # for i in range(len(self.args)):
#         return (f'{self.args[0]}\n {self.args[1]}'
#
#
# #        return f'{self.args}'
#
# a = Matrix([[1, 2, 3], [4, 5, 6]])
# print(a)
