# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
# характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий
# товаров. Пример:
# { “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000], “количество”: [5, 2, 7], “ед”: [“шт.”] }

computer_name = input("Введите название компьтера: ")
computer_price = input("Введите цену компьютера: ")
computer_count = input("Введите количество: ")
computer_unit = input("Введите единицы измерения: ")

printer_name = input("Введите название принтера: ")
printer_price = input("Введите цену принтера: ")
printer_count = input("Введите количество: ")
printer_unit = input("Введите единицы измерения: ")

scan_name = input("Введите название сканера: ")
scan_price = input("Введите цену сканера: ")
scan_count = input("Введите количество: ")
scan_unit = input("Введите единицы измерения: ")

computer_dict = {"название": computer_name, "цена": computer_price, "количество": computer_count, "ед": computer_unit}
printer_dict = {"название": printer_name, "цена": printer_price, "количество": printer_count, "ед": printer_unit}
scan_dict = {"название": scan_name, "цена": scan_price, "количество": scan_count, "ед": scan_unit}

computer_tuple = (1, computer_dict)
printer_tuple = (2, printer_dict)
scan_tuple = (3, scan_dict)
tuple_list = [computer_tuple, printer_tuple, scan_tuple]
print('\n'.join(map(str, tuple_list)))

category_name = [computer_dict["название"], printer_dict["название"], scan_dict["название"]]
category_price = [computer_dict["цена"], printer_dict["цена"], scan_dict["цена"]]
category_count = [computer_dict["количество"], printer_dict["количество"], scan_dict["количество"]]
category_unit = [computer_dict["ед"], printer_dict["ед"], scan_dict["ед"]]

category_dict = {"название": category_name, "цена": category_price, "количество": category_count, "ед": category_unit}
print(category_dict)