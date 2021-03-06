# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
# клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.

# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.

# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам.

# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
# аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
# строку: *****\n*****\n**.

# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n*****.

# Подсказка: подробный список операторов для перегрузки доступен по ссылке:
# https://pythonworld.ru/osnovy/peregruzka-operatorov.html

class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        my_add = self.count + other.count
        return my_add

    def __sub__(self, other):
        my_sub = self.count - other.count
        return my_sub

    def __mul__(self, other):
        my_mul = self.count * other.count
        return my_mul

    def __truediv__(self, other):
        my_truediv = self.count / other.count
        return int(round(my_truediv))

    def make_order(self, row):
        my_str = "*" * self.count
        return '\n'.join(my_str[el:el + row] for el in range(0, len(my_str), row))


my_cell = Cell(21)
my_cell_new = Cell(14)
print(f"Сложение:  {my_cell + my_cell_new}")
print(f"Вычитание: {my_cell - my_cell_new}")
print(f"Умножение: {my_cell * my_cell_new}")
print(f"Деление:   {my_cell / my_cell_new}")
print(f"Строка:\n{my_cell.make_order(8)}")