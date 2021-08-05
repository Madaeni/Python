# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

my_list = [randint(0, 1000) for el in range(randint(10, 14))]

with open("lesson-5-5.txt", "w") as number_list:
    number_list.write(" ".join(map(str, my_list)))

print("Список чисел:", " ".join(map(str, my_list)))
print(f"Сумма чисел: {sum(my_list)}")  # Легкий способ вывести сумму, если нам известен список заранее.

# Если список мы можем получить только из файла:

with open("lesson-5-5.txt", "r") as count:
    count_list = count.readline()
    count_list = count_list.split()
    count_list = list(map(int, count_list))

print(f"Сумма чисел: {sum(count_list)}")