def user_info():
    name = input('Введите Ваше имя: ')
    surname = input('Введите Вашу фамилию: ')
    year = input('Введите год Вашего рождения: ')
    town = input('Введите Ваш город проживания: ')
    email = input('Введите адрес Вашей элетронной почты: ')
    phone = input('Введите Ваш номер телефона: ')
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город проживания: {town}, Почта: {email}, Телефон: {phone}')
    return 
    
user_info()