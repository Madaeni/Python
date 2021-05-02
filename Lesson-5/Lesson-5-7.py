# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

my_list = []
profit_list = []

with open("lesson-5-7.txt", "r", encoding='utf-8') as company_list:
    while True:
        my_str = company_list.readline()
        my_str = my_str.split()
        if not my_str:
            break
        profit = int(my_str[2]) - int(my_str[3])
        my_dict = {my_str[0]: profit}
        my_list.append(my_dict)
        if profit > 0:
            profit_list.append(profit)

average_profit = list(map(int, profit_list))
average_profit = sum(average_profit)
profit_dict = {"average_profit": average_profit}
my_list.append(profit_dict)

with open("lesson-5-7.json", "w") as write_json:
    json.dump(my_list, write_json)

print(my_list)