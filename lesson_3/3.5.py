def my_sum():
    result = 0
    Q = False
    while Q == False:
        string = input('Для нахождения суммы введите числа через пробел. Для выхода нажмите Q').split(' ')
        for i in range(len(string)):
            if string[i].isdigit() == True:
                result += int(string[i])
            else:
                Q = True
        print(result)
    return 

my_sum()