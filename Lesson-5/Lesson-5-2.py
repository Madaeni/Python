# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

n = 0

with open("lesson-5-2.txt", "r") as my_file:
    while True:
        my_str = my_file.readline()
        sum_words = len(my_str.split())
        if not sum_words:
            break
        else:
            n += 1
            print(f"Количество слов в {n} равно {sum_words}")

print(f"Количество строк равно {n}")