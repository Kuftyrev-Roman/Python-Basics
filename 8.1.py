"""
1)	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Date:
    def __init__(self, data):
        self.date = data

    @classmethod
    def str_to_int(cls, data):
        date, month, year = [int(i) for i in data.split('-')]
        print(date, month, year)

    @staticmethod
    def date_valid(data):
        date, month, year = [int(i) for i in data.split('-')]
        if not 1 <= date <= 31:
            print('Вы ввели не коректное число.')
        else:
            print(date, end=' ')
        if not 1 <= month <= 12:
            print('Вы ввели не коректный номер месяца.')
        else:
            print(month, end=' ')
        if not 1920 <= year <= 2020:
            print('Вы ввели не коректный год.')
        else:
            print(year, end=' ')

Date.str_to_int('12-12-2020')
Date.date_valid('31-11-1920')
