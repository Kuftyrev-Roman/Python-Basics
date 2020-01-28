user_month = int(input('Введите номер месяца: '))
month = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if user_month in month[0:3]:
    print('Зима')
elif user_month in month[3:6]:
    print('Весна')
elif user_month in month[6:9]:
    print('Лето')
elif user_month in month[9:]:
    print('Осень')