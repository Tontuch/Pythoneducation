#4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go (self):
        if self.speed > 0:
            return 'Машина поехала'

    def stop (self):
        if self.speed == 0:
            return 'Машина остановилась'

    def turn_direction (self, direction):
        self.direction = direction
        if self.direction == 'left':
            return 'Машина повернула налево'
        elif self.direction == 'rigth':
            return 'Машина повернула направо'
        else:
            return 'Машина развернулась'

    def show_speed (self):
        return self.speed

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return 'Внимание привышение скорости!!'
        else:
            return self.speed
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'Внимание привышение скорости!!'
        else:
            return self.speed

car_1 = Car(100, "black", 'land cruiser', False)
car_2 = Car(80, "red", "Forester", True)
car_3 = Car(60, "white", "hino", False)
print(car_1.color, car_1.speed, car_1.name)
print(car_1.go())
print(car_2.turn_direction('rigth'))

car_4 = TownCar(100, 'black', 'crown', False)
print(car_4.show_speed())
print(car_1.show_speed())
car_5 = WorkCar(60, "white", "hino", False)
print(car_5.show_speed())


