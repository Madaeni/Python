# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.


def my_sum(arg):
    arg = list(map(int, arg))
    my_result = sum(arg)
    return print(my_result)


while True:
    number_str = input("Веедите несколько чисел через пробел. Для завершения введите букву s: ")
    my_list = number_str.split()
    my_symbol = my_list[-1]

    if "s" in my_list:
        stop_word = my_list.index("s")
        del my_list[stop_word:]
        my_sum(my_list)
        break
    else:
        my_sum(my_list)
