# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def divide(arg_one, arg_two):
    return arg_one / arg_two


while True:
    number_one = int(input("Введите первое число: "))
    number_two = int(input("Введите второе число: "))
    if number_two == 0:
        print("Введите иное второе число, так как на ноль не делят")
    else:
        print(divide(number_one, number_two))
        break
