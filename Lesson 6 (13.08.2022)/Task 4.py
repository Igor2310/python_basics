# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,                                                                               остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.
from random import choice


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self):
        print(f"Машина повернула {choice(['влево', 'вправо'])}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print("Превышение скорости > 60") if self.speed > 60 else print(self.speed)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print("Превышение скорости > 40") if self.speed > 40 else print(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


class SportCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, name="Sport car")


towncar1 = TownCar(70, "Red", "Peugeot")
workcar1 = WorkCar(70, "White", "Lada")
policecar1 = PoliceCar(70, "White", "Hyundai")
sportcar1 = SportCar(70, "White")

for i in (towncar1, workcar1, policecar1, sportcar1):
    i.go(), i.stop(), i.turn(), i.show_speed()
    print(i.speed, i.color, i.name, i.is_police)
    print("-" * 20)
