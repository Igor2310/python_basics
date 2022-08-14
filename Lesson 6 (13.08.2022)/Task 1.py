# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
import time


class TrafficLight:
    __color = {"Red": 7, "Yellow": 2, "Green": 1}

    def running(self, count):
        try:
            count = eval(count)
        except NameError:
            pass
        if type(count) == int and count > 0:
            i = 0
            while i != count:
                [(print(key), time.sleep(value)) for key, value in self.__color.items()]
                i += 1
            del i
        else:
            print("Number must be int and more 0")


traffic_number1 = TrafficLight()
traffic_number1.running(input("enter the number of traffic light cycles "))
