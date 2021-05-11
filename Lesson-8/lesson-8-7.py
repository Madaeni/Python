# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, arg_1, arg_2):
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    def __add__(self, other):
        my_num_1 = self.arg_1 + other.arg_1
        my_num_2 = self.arg_2 + other.arg_2
        return complex(my_num_1, my_num_2)

    # Формула взята с https://ru.wikipedia.org/wiki/Комплексное_число
    def __mul__(self, other):
        my_num_1 = self.arg_1 * other.arg_1 - self.arg_2 * other.arg_2
        my_num_2 = self.arg_2 * other.arg_1 + self.arg_1 * other.arg_2
        return complex(my_num_1, my_num_2)


my_complex_num_1 = ComplexNumber(2, -1)
my_complex_num_2 = ComplexNumber(5, 8)

print(my_complex_num_1 + my_complex_num_2)
print(my_complex_num_1 * my_complex_num_2)