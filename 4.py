user_number = input('Введите целое положительное число: ')
numbers = ['9', '8','7','6','5','4','3','2','1','0']
i = 0
for i in range(10):
    if numbers[i] in user_number:
        print('Самая большая цифра в вашем числе: ', numbers[i])
        break
else:
    i += 1
