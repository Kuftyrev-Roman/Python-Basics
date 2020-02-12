"""
5)	Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Пишу ручкой')


class Pencil(Stationery):

    def draw(self):
        print('Пишу карандашом')


class Handle(Stationery):
    def draw(self):
        print('Пишу маркером')

Bic = Stationery('Bic')
Flair = Pen('Flair')
DKNY = Pencil('DKNY')
Copic = Handle('Copic')

Bic.draw()
Flair.draw()
DKNY.draw()
Copic.draw()
