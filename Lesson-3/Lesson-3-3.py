# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(arg_one, agr_two, arg_three):
    min_number = min(arg_one, agr_two, arg_three)
    return print(arg_one + agr_two + arg_three - min_number)


first = int(input("Первое число: "))
second = int(input("Второе число: "))
third = int(input("Третье число: "))

my_func(first, second, third)