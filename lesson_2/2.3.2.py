user_month = int(input('Введите номер месяца: '))
month = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5),'Лето': (6, 7, 8),'Осень': (9, 10, 11),}
if user_month in month['Зима']:
    print('Зима')
elif user_month in month['Весна']:
    print('Весна')
elif user_month in month['Лето']:
    print('Лето')
elif user_month in month['Осень']:
    print('Осень')