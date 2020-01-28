user_time = int(input('Введите время в секундах: '))
ours = user_time // 3600
minute = user_time // 60 - ours*60
second = user_time % 60
print(f'{ours}:{minute}:{second}')
