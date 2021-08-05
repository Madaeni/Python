# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def extract(cls, param):
        my_day, my_month, my_year = map(int, param.split("-"))
        return print(f"Разбивка на числа: день - {my_day}, месяц - {my_month}, год - {my_year}")

    @staticmethod
    def validation(param):
        my_day, my_month, my_year = map(int, param.split("-"))
        if my_year % 4 == 0 and my_month == 2 and 0 < my_day <= 29:
            print(f"{param} високосный год")
        elif 0 < my_day <= 31 and 0 < my_month <= 12 and my_month != 2:
            print(f"{param} год не високосный")
        else:
            print("Неверная дата")


# my_calendar = "29-03-2014"
my_calendar = input("Веддите дату через дефис (например 29-03-2014): ")
my_data = Data(my_calendar)
my_data.extract(my_calendar)
my_data.validation(my_calendar)
