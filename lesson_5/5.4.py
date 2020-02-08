"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""

with open('numbers.txt',encoding='utf-8') as f:
    eng = ['One', 'Two', 'Three', 'Four']
    rus = ['Один', 'Два', 'Три', 'Четыре']
    i = 0
    mod_string = []
    for line in f:
        string = line.replace(eng[i], rus[i])
        mod_string.append(string)
        i += 1

    with open('mod_numbers.txt', 'w', encoding='utf-8') as out:
        out.writelines(mod_string)

