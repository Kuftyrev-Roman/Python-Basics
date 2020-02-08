"""
3)	Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open('salary.txt', encoding='utf-8') as f:
    staff = {}
    for string in f:
        strings = string.strip()
        employee = strings.split()
        staff.update({employee[0]: float(employee[1])})

    print('Фамилии сотрудников с окладом менее 20000: ')
    for key, value in staff.items():
        if value < 20000:
            print(f'{key}, ', end='')

    average_salary = round(sum(staff.values()) / len(staff), 2)
    print(f'\nСредняя величина дохода сотрудников: {average_salary}')
