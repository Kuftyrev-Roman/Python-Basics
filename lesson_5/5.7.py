"""
7)	Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
"""

with open('firm_list.txt', encoding='utf-8') as inf:
    profit = []
    firm_list = {}
    for line in inf:
        split_line = line.split()
        firm_profit = int(split_line[2]) - int(split_line[3])
        profit.append(firm_profit)
        print(f'Прибыль {split_line[1]} {split_line[0]} составила {firm_profit}')
    positive_profit = [i for i in profit if i > 0]
    avarage_profit = sum(positive_profit) / len(positive_profit)
    print(f'Средняя прибыль компаний равна: {avarage_profit}')
