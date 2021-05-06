# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = int(wage)
        self.bonus = int(bonus)
        _income = {"Оклад": wage, "Премия": bonus}
        print(f"Имя: {self.name} \nФамилия: {self.surname} \nДолжность: {self.position} \nДоход: {_income}")


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имени сотрудника: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход с учетом премии: {self.wage + self.bonus}")


my_position = Position("John", "Doe", "Worker", 10000, 5000)
my_position.get_full_name()
my_position.get_total_income()