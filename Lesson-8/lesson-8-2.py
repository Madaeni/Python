# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class DivideZero(Exception):
    def __init__(self, txt):
        self.txt = txt


my_num_1 = int(input("Введите первое число: "))
my_num_2 = int(input("Введите втрое число: "))

try:
    if my_num_2 == 0:
        raise DivideZero("На ноль делить нельзя!")
except DivideZero as err:
    print(err)
else:
    print(round(my_num_1 / my_num_2, 2))