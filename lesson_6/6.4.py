"""
4)	Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:

    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        else:
            print(self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
        else:
            print(self.speed)

class PoliceCar(Car):
    pass


Lada = TownCar(65, 'Баклажан', 'Гранта', False)
Bugatti = SportCar(250, 'Лазурный', 'Chiron', False)
Kamaz = WorkCar(70, 'Жёлтый', 'Камаз-4308', False)
Mercedes = PoliceCar(200, 'Бело-синий', 'AMG GLS 63', True)

print(Lada.name)
print(Lada.colour)
Lada.go()
Lada.turn('влево')
Lada.show_speed()
print(Lada.is_police)

Bugatti.show_speed()
print(Bugatti.colour)
Bugatti.stop()

Kamaz.show_speed()

print(Mercedes.is_police)
