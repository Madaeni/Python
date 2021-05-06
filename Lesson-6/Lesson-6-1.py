# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.
from time import sleep


class TrafficLight:
    __color = None

    def running(self, color):
        self.__color = color
        if color == "red":
            self.__color = "red"
            print("Красный")
            sleep(7)
            self.__color = "yellow"
            print("Желтый")
            sleep(2)
            self.__color = "green"
            print("Зеленый")
            sleep(7)
        elif color == "yellow":
            self.__color = "yellow"
            print("Желтый")
            sleep(2)
            self.__color = "green"
            print("Зеленый")
            sleep(7)
            self.__color = "red"
            print("Красный")
            sleep(7)
        else:
            self.__color = "green"
            print("Зеленый")
            sleep(7)
            self.__color = "red"
            print("Красный")
            sleep(7)
            self.__color = "yellow"
            print("Желтый")
            sleep(2)

        """Если нужно запустить в бесконечном цикле:
        while True:
            self.running()"""


traffic_light = TrafficLight()
print(traffic_light.running("red"))