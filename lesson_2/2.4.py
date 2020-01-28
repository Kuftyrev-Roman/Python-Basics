user_string = input('Введите строку: ').split()
for i in range(len(user_string)):
    if len(user_string[i]) > 10:
        print(i, user_string[i][:10])
        continue
    print(i, user_string[i])