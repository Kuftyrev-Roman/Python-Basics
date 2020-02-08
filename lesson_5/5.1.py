"""
1)	Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('user_info.txt', 'w') as ouf:
    while True:
        string = input('Enter your text: ')
        print(string, file=ouf)
        if not string.isalnum():
            break
