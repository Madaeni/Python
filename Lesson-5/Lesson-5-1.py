# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

with open("Lesson-5-1.txt", "w") as my_list:
    while True:
        my_str = input("Введите данные или оставьте пустой для выхода: ")
        if not my_str:
            break
        else:
            my_list.write(my_str + '\n')