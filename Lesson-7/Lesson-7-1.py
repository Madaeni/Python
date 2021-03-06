# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

# Примеры матриц вы найдете в методичке.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
# матриц). Результатом сложения должна быть новая матрица.

# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, sheet_lists):
        self.sheet_lists = sheet_lists

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, lists)) for lists in self.sheet_lists])

    def __add__(self, other):
        return Matrix(list(map(lambda a, b: list(map(lambda x, y: x + y, a, b)), self.sheet_lists, other.sheet_lists)))


my_matrix = Matrix([[-5, 2, 1], [-4, 8, 2], [9, 3, -7]])
my_matrix_new = Matrix([[7, 7, 5], [4, -6, 1], [-5, 0, 9]])
print(my_matrix + my_matrix_new)