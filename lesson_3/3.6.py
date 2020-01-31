def int_func(word): 
    return word.title()
    
def func():
    string = input('Введите строку: ').split(' ')
    for i in range(len(string)):
        print(int_func(string[i]), end =' ')
    return

func()