# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина *
# масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    _length = None
    _width = None
    _height = None
    __road_mass = 25

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def calc(self):
        road_mass_height = (self._length * self._width * self.__road_mass * self._height) // 1000
        print(f"Масса асфальта для покрытия заданной дороги равна {road_mass_height}т")


road_length = int(input("Введите длинну дороги: "))
road_width = int(input("Введите ширину дороги: "))
road_height = int(input("Введите толщину дороги: "))
my_road = Road(road_length, road_width, road_height)
my_road.calc()
