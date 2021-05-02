# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
ru_list = open("lesson-5-4-ru.txt", "w")

with open("lesson-5-4-eng.txt", "r") as eng_list:
    while True:
        my_str = eng_list.readline()
        my_str = my_str.split()
        if not my_str:
            break
        if my_str[0] in my_dict:
            my_str[0] = my_dict[my_str[0]]
            ru_list.write(' '.join(my_str) + '\n')

ru_list.close()