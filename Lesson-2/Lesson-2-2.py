# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

my_list = input("Введите список: ")
ele_list = list(my_list)
count_list = len(ele_list)
ele_index = 0

for ele in range(count_list - 1):
    if ele_index % 2 == 0:
        ele_list[ele_index], ele_list[(ele_index + 1)] = ele_list[(ele_index + 1)], ele_list[ele_index]
    ele_index += 1
print(ele_list)