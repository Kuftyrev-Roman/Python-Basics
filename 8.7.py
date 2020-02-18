"""
7)	Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNum:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def __str__(self):
        return f'{self.Re}+{self.Im}i'

    def __add__(self, other):
        result = ComplexNum((self.Re + other.Re), (self.Im + other.Im))
        return result

    def __mul__(self, other):
        result = ComplexNum((self.Re * other.Re - self.Im * other.Im), (self.Re * other.Im + self.Im * other.Re))
        return result


a = ComplexNum(2, 3)
b = ComplexNum(1, 2)
c = ComplexNum(7, 5)
print(a + b + c)
print(a * b)
