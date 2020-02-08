"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('num_for_sum.txt', 'w') as num:
    series = [i for i in range(101)]
    for i in series:
        print(i, end=' ', file=num)

with open('num_for_sum.txt') as num:
    num_for_sum = num.read().split()
    summa = 0
    for i in num_for_sum:
        summa += int(i)
    print(summa)
