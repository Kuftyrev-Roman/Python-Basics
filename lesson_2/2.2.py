my_list = list(input('Введите элементы списка: '))
i = 0
j = 1
while j < len(my_list):
    my_list[i], my_list[j] = my_list[j], my_list[i]
    i += 2
    j += 2
print(my_list)
