def my_division():
    arg_1 = float(input('Введите первое число: '))
    arg_2 = float(input('Введите второе число: '))
    while arg_2 == 0:
        arg_2 = float(input('Введите второе число отличное от нуля: '))
    else:
        result = arg_1 / arg_2
    return round(result, 2)
    
print(my_division())
