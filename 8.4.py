"""
4)	Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5)	Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
6)	Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""
class Warehouse:
    office_equipment = {}
    dep_equipment = {}

    def reception(self, name: str, amount: int):
        self.name = name
        self.amount = amount
        if self.name not in Warehouse.office_equipment:
            Warehouse.office_equipment[self.name] = self.amount
        else:
            Warehouse.office_equipment[self.name] = self.amount

    def transfer(self, department, name: str, amount: int):
        self.department = department
        self.name = name
        self.amount = amount
        if self.name not in Warehouse.office_equipment or Warehouse.office_equipment[self.name] < 1:
            print('Такого оборудования нет на складе.')
        elif Warehouse.office_equipment[self.name] < self.amount:
            print('Оборудования на складе не достаточно.')
        else:
            Warehouse.office_equipment[self.name] -= self.amount
            Warehouse.dep_equipment[self.department][self.name] += self.amount


class OfficeEquipment:

    def __init__(self, id, name, cost):
        self.id = id
        self.name = name
        self.cost = cost

    def __str__(self):
        return f'{self.id}, {self.name}, {self.cost}'


class Printer(OfficeEquipment):
    def __init__(self, id, name, cost, speed):
        self.speed = speed
        OfficeEquipment.__init__(self, id, name, cost)

    def __str__(self):
        return f'{self.id}, {self.name}, {self.cost}, {self.speed}'

class Scaner(OfficeEquipment):
    def __init__(self, id, name, cost, resolution):
        self.resolution = resolution
        OfficeEquipment.__init__(self, id, name, cost)

    def __str__(self):
        return f'{self.id}, {self.name}, {self.cost}, {self.resolution}'

class Xerox(OfficeEquipment):
    def __init__(self, id, name, cost, colour):
        self.colour = colour
        OfficeEquipment.__init__(self, id, name, cost)

    def __str__(self):
        return f'{self.id}, {self.name}, {self.cost}, {self.colour}'


phone = OfficeEquipment(1, "Panasonic", 1500)
brother = Printer(2, 'Brother', 5000, 13)
hp = Printer(3, 'HP', 2000, '1800x1200')
xerox = Xerox(4,'Xerox', 7900, 'monochrome')

print(phone)
print(brother)
print(hp)
