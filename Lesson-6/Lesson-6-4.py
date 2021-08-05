# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, color, speed, direction, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.__direction = direction
        self.__is_police = is_police
        print(f"Тип: {self.name}\nЦвет: {self.color}")

    def go(self):
        if self.speed > 0:
            print("Автомобиль движется")

    def stop(self):
        if self.speed == 0:
            print("Автомобиль остановился\n")

    def turn(self):
        if self.speed > 0:
            if self.__direction == "лево" or self.__direction == "влево" or self.__direction == "налево":
                print("Автомобиль повернул налево\n")
            elif self.__direction == "право" or self.__direction == "вправо" or self.__direction == "направо":
                print("Автомобиль повернул направо\n")
            else:
                print("Автомобиль двигается по прямой\n")

    def show_speed(self):
        print(f"Скорость автомобиля равна: {self.speed} км/ч")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Вы превысили скорось на {self.speed - 60} км/ч")
        else:
            print(f"Скорость автомобиля равна: {self.speed} км/ч")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Вы превысили скорось на {self.speed - 40} км/ч")
        else:
            print(f"Скорость автомобиля равна: {self.speed} км/ч")


my_sport_car = SportCar("Спотривныый автомобиль", "Желтый", 140, "прямо", False)
my_sport_car.go()
my_sport_car.show_speed()
my_sport_car.stop()
my_sport_car.turn()

my_police_car = PoliceCar("Полицейский автомобиль", "Белый", 0, "прямо", True)
my_police_car.go()
my_police_car.show_speed()
my_police_car.stop()
my_police_car.turn()

my_town_car = TownCar("Городской автомобиль", "Красный", 60, "право", False)
my_town_car.go()
my_town_car.show_speed()
my_town_car.stop()
my_town_car.turn()

my_work_car = WorkCar("Рабочий автомобиль", "Синий", 50, "лево", False)
my_work_car.go()
my_work_car.show_speed()
my_work_car.stop()
my_work_car.turn()
