# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, param):
        self.param = param


class Coat(Clothes):
    @property
    def sewing(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    @property
    def sewing(self):
        return 2 * self.param + 0.3


my_coat = Coat(45)
my_suit = Suit(1.8)
print(round(my_coat.sewing, 2))
print(round(my_suit.sewing, 2))
print(round(my_suit.sewing + my_coat.sewing, 2))