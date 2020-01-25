debit = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите значение издержек фирмы: '))
if debit > costs:
    print('Фирма приносит прибыль.')
    profit = debit / costs
    print('Рентабельность составляет: ', profit)
    staff = int(input('Введите количество сотрудников фирмы: '))
    profit_per_unit = debit / staff
    print('Прибыль фирмы в расчете на одного сотрудника составляет: ', profit_per_unit)
if debit < costs:
    print('Фирма приносит убыток.')
