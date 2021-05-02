# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_list = []
my_list_sum = []
my_list_name = []
my_dict = {}

with open("lesson-5-6.txt", "r", encoding='utf-8') as timetable:
    while True:
        my_str = timetable.readline()
        my_str = my_str.replace(":", "")
        my_str = my_str.replace("(л)", "")
        my_str = my_str.replace("(пр)", "")
        my_str = my_str.replace("(лаб)", "")
        my_str = my_str.replace("-", "0")
        my_timetable = my_str.split()
        if not my_str:
            break
        my_list.append(my_timetable)

for el in my_list:
    dict_name = el[0]
    list_el = el.pop(0)
    el = list(map(int, el))
    sum_el = sum(el)
    my_list_sum.append(sum_el)
    my_list_name.append(dict_name)

my_dict = dict(zip(my_list_name, my_list_sum))

print(my_dict)